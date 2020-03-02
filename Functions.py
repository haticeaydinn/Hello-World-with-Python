def greet_user():
    print("Hello there!")
    print("Welcome abroad!")


greet_user()


# with parameters
def greet_user2(name):
    print(f'Hello {name}!')  # same as a local variable in function: name = "Hatice"
    print("Welcome abroad!")


greet_user2("Hatice")


# with keyword arguments and we dont care about the order of parameters
def greet_user3(first_name, last_name):
    print(f'Hello {first_name} {last_name}!')
    print("Welcome abroad!")


greet_user3(last_name="Ay", first_name="Hatice")
