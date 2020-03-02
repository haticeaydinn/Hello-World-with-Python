message = input(">")
words = message.split(" ")  # split method turns a list and it splits strings
print(words)

emoji_mapping = {
    ":)": "😊",  # windows 10 emoji shortcut: windows + .
    ":(": "😢",
    ":/": "😒"
}

output = ""
for char in words:
    output += emoji_mapping.get(char, char) + " "
print(output)
