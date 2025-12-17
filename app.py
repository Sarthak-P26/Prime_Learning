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

def replay():
    while True:
        try:
            choice = input("You wanna try is again Y/N: ").lower()
        except ValueError:
            print("Enter the valid value")
        if choice in ("y", "yes"):
            loop = True
            break
        elif choice in ("n", "no"):
            loop = False
            break
        else:
            print("Enter the valid input....")
    return loop


print("Check Prime or Not Prime 🕵️  🕵️")

def main():
    loop = 1
    while loop:
        number = take_input()
        if number <= 2:
            isprime = set_output(number)
        else:
            isprime = unknown_output(number)
        
        result_showing(number, isprime)

        loop = replay()
        
if __name__ == "__main__": 
    main()

