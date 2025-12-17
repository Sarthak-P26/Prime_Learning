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

def run_loop():
    while True:
        try:
            choice = input("You wanna try is again Y/N: ")
        except ValueError:
            print("Enter the valid value")
        if choice == "Y" or "Yes":
            loop = True
            break
        elif choice == "N" or "No":
            loop = False
            break
        else:
            continue
    return loop


print("Check Prime or Not Prime 🕵️  🕵️")

def main():
    number = take_input()
    if number <= 2:
        isprime = set_output(number)
    else:
        isprime = unknown_output(number)
    
    result_showing(number, isprime)

    

main()


# play = True
# while play:
    

#     user = input("You want to test another number: (yes/no)").lower()
#     if user == 'yes':
#         continue
#     else:
#         play = False