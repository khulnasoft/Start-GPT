## 💾 Installation

To install Start-GPT, follow these steps:

0. Make sure you have all the **requirements** above, if not, install/get them.

*The following commands should be executed in a CMD, Bash or Powershell window. To do this, go to a folder on your computer, click in the folder path at the top and type CMD, then press enter.*

1. Clone the repository:
For this step you need Git installed, but you can just download the zip file instead by clicking the button at the top of this page ☝️
```
git clone https://github.com/khulnasoft/Start-GPT.git
```

2. Navigate to the project directory:
*(Type this into your CMD window, you're aiming to navigate the CMD window to the repository you just downloaded)*
```
cd 'Start-GPT'
```

3. Install the required dependencies:
*(Again, type this into your CMD window)*
```
pip install -r requirements.txt
```

4. Rename `.env.template` to `.env` and fill in your `OPENAI_API_KEY`. If you plan to use Speech Mode, fill in your `ELEVEN_LABS_API_KEY` as well.
  - Obtain your OpenAI API key from: https://platform.openai.com/account/api-keys.
  - Obtain your ElevenLabs API key from: https://elevenlabs.io. You can view your xi-api-key using the "Profile" tab on the website.
  - If you want to use GPT on an Azure instance, set `USE_AZURE` to `True` and provide the `OPENAI_AZURE_API_BASE`, `OPENAI_AZURE_API_VERSION` and `OPENAI_AZURE_DEPLOYMENT_ID` values as explained here: https://pypi.org/project/openai/ in the `Microsoft Azure Endpoints` section