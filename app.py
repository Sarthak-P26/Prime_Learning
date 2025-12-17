def take_input():
    try:
        number = int(input("Enter the number: "))
    except ValueError:
        print("Enter the valid value")
    return number


def set_output(number):
    if number <= 1:
        is_prime = False
    elif number == 2:
        is_prime = True
    return is_prime


def unknown_output(number):
    for item in range(2, number):
        if number % item == 0:
            isprime = False
            break
        else:
            isprime = True
    return isprime 


def result_showing(number, isprime):
    if isprime == True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


print("Check Prime Or Not")



# play = True
# while play:
    

#     user = input("You want to test another number: (yes/no)").lower()
#     if user == 'yes':
#         continue
#     else:
#         play = False