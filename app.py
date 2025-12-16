print("Welcome To Check Your Number Is Prime Or Not")

# Take an input from a user.
number = int(input("Enter a number: "))

if number <= 1:
    print("Enter the number greater than 1")
elif number == 2: 
    print("2 is a prime number...")


for serial_no in range(2, number -1):
    if number % serial_no == 0:
        print("It's not a prime number")
    else:
        print("It's a prime number")


