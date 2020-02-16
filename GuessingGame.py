guess_count = 0
magic_number = 9
guess_limit = 3

while guess_count < guess_limit:
    guessed_number = int(input("Guess: "))
    guess_count += 1
    if guessed_number == magic_number:
        print("You won!!!")
        break
else:
    print("You failed...")
