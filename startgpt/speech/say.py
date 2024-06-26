""" Text to speech module """
import threading
from threading import Semaphore

from startgpt.config.config import Config
from startgpt.speech.base import VoiceBase
from startgpt.speech.eleven_labs import ElevenLabsSpeech
from startgpt.speech.gtts import GTTSVoice
from startgpt.speech.macos_tts import MacOSTTS
from startgpt.speech.stream_elements_speech import StreamElementsSpeech

_QUEUE_SEMAPHORE = Semaphore(
    1
)  # The amount of sounds to queue before blocking the main thread


def say_text(text: str, config: Config, voice_index: int = 0) -> None:
    """Speak the given text using the given voice index"""
    default_voice_engine, voice_engine = _get_voice_engine(config)

    def speak() -> None:
        success = voice_engine.say(text, voice_index)
        if not success:
            default_voice_engine.say(text)

        _QUEUE_SEMAPHORE.release()

    _QUEUE_SEMAPHORE.acquire(True)
    thread = threading.Thread(target=speak)
    thread.start()


def _get_voice_engine(config: Config) -> tuple[VoiceBase, VoiceBase]:
    """Get the voice engine to use for the given configuration"""
    tts_provider = config.text_to_speech_provider
    if tts_provider == "elevenlabs":
        voice_engine = ElevenLabsSpeech(config)
    elif tts_provider == "macos":
        voice_engine = MacOSTTS()
    elif tts_provider == "streamelements":
        voice_engine = StreamElementsSpeech()
    else:
        voice_engine = GTTSVoice()

    return GTTSVoice(), voice_engine
