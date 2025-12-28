def take_input():
    '''Take input: history or Number'''
    while True:
            user_input = input("Enter a 'h' for history (Or) number: ")
            if user_input.isdigit() or user_input.lower() in ('history', 'History', 'h'):
                return user_input
            else:
                print("Invalid input...")

def set_output(input_number):
    '''input_number < 1 = Not Prime (or) input_number ==2 = Prime'''
    if input_number <= 1:
        return False
    elif input_number == 2:
        return True
        
def unknown_output(input_number):
    '''Finding the prime or Not Prime'''
    for item in range(2, input_number):
        if input_number % item == 0:
            return False
    return True
    
def result_showing(input_number, isprime):
    '''Printing The output and return it '''
    if isprime :
        print(f"{input_number} It's a prime number")
        return "It's prime"
    else:
        print(f"{input_number} is not a prime number")
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
        print("Sorry file is not available \nRestart the Program")

def history_printer():
    '''Print the history on user input'''
    filename = 'history.txt'
    with open(filename) as file_object:
        print(file_object.read())

print("Check Prime or Not Prime 🕵️  🕵️")

def main():
    '''This the main function'''
    history_header()
    line_counter = count_giver()
    replay_input = True
    while replay_input:
        user_input = take_input()
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input <= 2:
                isprime = set_output(user_input)
            else:
                isprime = unknown_output(user_input)
            
            solution = result_showing(user_input, isprime)
            
            with open("history.txt", "a") as h:
                h.write(f"\t{line_counter}) {user_input} = {solution} \n")
            
            replay_input = replay() 
            line_counter += 1
        
        elif user_input.lower() in ("history", "History", 'h') :
            print("This is your full history")
            history_printer()
            replay_input = replay() 
                    
if __name__ == "__main__": 
    main()
    


