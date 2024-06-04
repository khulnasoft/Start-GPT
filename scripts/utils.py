def clean_input(prompt: str=''):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("You interrupted Start-GPT")
        print("Quitting...")
        exit(0)
