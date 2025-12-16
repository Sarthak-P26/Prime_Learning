print("Welcome To Check Your Number Is Prime Or Not")
play = True
while play:
    

    # Take an input from a user.
    number = int(input("Enter a number: "))

    if number <= 1:
        print("Enter the number greater than 1")
    elif number == 2: 
        print("2 is a prime number...")


    for serial_no in range(2, number):
        if number % serial_no == 0:
            value = False
            break
        
        else:
            value = True


    if value == True:
        print("It's a prime number")
    else:
        print("It's not a prime number")

    user = input("You want to test another number: (yes/no)").lower()
    if user == 'yes':
        continue
    else:
        play = False