def take_input():
    '''Take input: history or Number'''
    while True:
            user_input = input("Enter a 'h' for history (Or) number: ")
            if user_input.isdigit() or user_input.lower() in ('history', 'History', 'h'):
                return user_input
            else:
                print("Invalid input...")

def set_output(input):
    '''input < 1 = Not Prime (or) input ==2 = Prime'''
    if input <= 1:
        return False
    elif input == 2:
        return True
    
def unknown_output(input):
    '''Finding the prime or Not Prime'''
    for item in range(2, input):
        if input % item == 0:
            return False
    return True
    
def result_showing(input, isprime):
    '''Printing The output and return it '''
    if isprime == True:
        print(f"{input} It's a prime number")
        return "It's prime"
    else:
        print(f"{input} is not a prime number")
        return "It's not prime"

def replay():
    '''Taking input for replay the program.'''
    while True:
        choice = input("You wanna try is again Y/N: ").lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("Enter the valid input....")
    
def history_header():
    '''If history file is empty add a header to it'''
    try:
        with open("history.txt", "r+") as t:
            # !!! Need improvement !!! (read the lines and then check file empty)
            if (len(t.readlines()) <= 0): # Change the logic for this line
                t.write("History saves here: \n")
    except FileNotFoundError:
        print("Sorry file is not available")

def count_giver():
    '''Creatinga couter for history writing'''
    try:     
        with open("history.txt") as f:
            lines = f.readlines()
            return ((len(lines)) - 1)
    except FileNotFoundError:
        print("Sorry file is not available")

def history_printer(user_input):
    '''Print the history on user input'''
    filename = 'history.txt'
    with open(filename) as file_object:
        print(file_object.read())

print("Check Prime or Not Prime 🕵️  🕵️")

def main():
    '''This the main function'''
    history_header()
    count = count_giver()
    loop = 1
    while loop:
        input = take_input()
        if input.isdigit():
            input = int(input)
            if input <= 2:
                isprime = set_output(input)
            else:
                isprime = unknown_output(input)
            
            solution = result_showing(input, isprime)
            
            with open("history.txt", "a") as h:
                h.write(f"\t{count}) {input} = {solution} \n")
            
            loop = replay() 
            count += 1
        
        elif input.lower() in ("history", "History", 'h') :
            print("This is your full history")
            history_printer(input)
            loop = replay() 
                    
if __name__ == "__main__": 
    main()
    


