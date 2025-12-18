def take_input():
    while True:
        try:
            return int(input("Enter the number: "))
        except ValueError:
            print("Enter the valid value.")


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
        print(f"{number} It's a prime number")
        solution_variable = "It's prime"
        return  solution_variable
    else:
        print(f"{number} is not a prime number")
        soluction_second = "It's not prime"
        return  soluction_second

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

def history_header():
    try:
        with open("history.txt", "r+") as t:
            if (len(t.readlines()) <= 0):
                t.write("History saves here: \n")
    except FileNotFoundError:
        print("Sorry file is not available")

def count_giver():
    try:     
        with open("history.txt") as f:
            lines = f.readlines()
            return ((len(lines)) - 1)
    except FileNotFoundError:
        print("Sorry file is not available")


print("Check Prime or Not Prime 🕵️  🕵️")

def main():
    
    history_header()
    
    count = count_giver()

    loop = 1
    while loop:
        number = take_input()
        if number <= 2:
            isprime = set_output(number)
        else:
            isprime = unknown_output(number)
        
        solution = result_showing(number, isprime)
       
        loop = replay() 
        count += 1
        with open("history.txt", "a") as h:
            h.write(f"\t{count}) {number} = {solution} \n")
        
             
if __name__ == "__main__": 
    main()
    


