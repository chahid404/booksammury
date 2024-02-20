import g4f

g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = True  # Disable automatic version checking

def chat_with_chatgpt4(message):
    return g4f.ChatCompletion.create(
        model="gpt-4",
        provider=g4f.Provider.Bing,
        messages=[{"role": "user", "content": message}]
        )