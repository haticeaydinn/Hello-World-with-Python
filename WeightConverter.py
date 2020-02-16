while True:
    weight = int(input("Your Weight: "))
    unit = input("(L)bs or (K)g ? ")

    if unit.upper() == "K":
        converted = weight / 0.45359237
        converted_update = format(converted, '.2f')  # take 2 digits in a floating number
        print(f"You are {converted_update} lbs")
    elif unit.upper() == 'L':
        converted = weight * 0.45359237
        converted_update = format(converted, '.2f')  # take 2 digits in a floating number
        print(f"You are {converted_update} kilos")
    else:
        print("You entered wrong unit type... Please only enter (L) or (K). ")

    is_quit = input("To continue, enter 'c'. To quit, enter 'q' : ")

    if is_quit == "q":
        break
