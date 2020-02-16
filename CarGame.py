my_input = ""
car_started = False

while my_input != "quit":
    my_input = input("> ").lower()

    if my_input == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')  # çoklu satırlı kodlarda girintiler kod içinde nasılsa, o şekilde görünür
    elif my_input == "start":
        if car_started:
            print("Car already started...")
        else:
            car_started = True
            print("Car started... Ready to go!")
    elif my_input == "stop":
        if not car_started:
            print("Car already stopped...")
        else:
            car_started = False
            print("Car stopped.")
    elif my_input == "quit":
        break
    else:
        print("I don't understand that...")
