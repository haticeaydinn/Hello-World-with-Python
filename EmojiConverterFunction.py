def emoji_converter(message):
    words = message.split(" ")
    emoji_mapping = {
        ":)": "😊",  # windows 10 emoji shortcut: windows + .
        ":(": "😢",
        ":/": "😒"
    }
    output = ""
    for char in words:
        output += emoji_mapping.get(char, char) + " "
    return output


message = input("> ")
print(emoji_converter(message))
