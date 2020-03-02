phone = input("Phone: ")

number_dic = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""
for numbers in phone:
    output += number_dic.get(numbers, "?") + " "  # add ? for unknown characters
print(output)
