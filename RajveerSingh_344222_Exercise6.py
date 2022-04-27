# Simple calculator in python

# Creating a list for past answers
answers = []

# Creating a loop for the calculator
while True:
    calculation = input("""Please choose the calculation method:
    + to add
    - to subtract
    * to multiply
    / to divide
    h to view past answers
    q to quit
    \n""")
        
    # For user to quit the calculator
    if calculation == 'q':
        break
    
    # Addition operation
    if calculation == '+':
        number1 = float(input("Enter the 1st number: "))
        number2 = float(input("Enter the 2nd number: "))
        result = number1 + number2
        print(result)
    
    # Subtraction operation
    elif calculation == '-':
        number1 = float(input("Enter the 1st number: "))
        number2 = float(input("Enter the 2nd number: "))
        result = number1 - number2
        print(result)
    
    # Multiplicatiopn operation
    elif calculation == '*':
        number1 = float(input("Enter the 1st number: "))
        number2 = float(input("Enter the 2nd number: "))
        result = number1 * number2
        print(result)
    
    # Division operation
    elif calculation == '/':
        number1 = float(input("Enter the 1st number: "))
        number2 = float(input("Enter the 2nd number: "))
        result = number1 / number2
        print(result)
    
    # For user to view the past answers
    elif calculation == 'h':
        if (len(answers) == 0):
            print("No past answers")
            break
        else:
            print("\nAll past answers are shown below\n")
            for x in answers:
                print(x)
    
    # If user did not choose an operator
    else:
        print("Invalid, no arithmetic operator was chosen.")
    
    # Append all answers to the list
    answers.append(result)
    
    calculate_again = input("""Return to the calculator menu? (y/n) """)
    
    # When user types "y", calculator starts
    if calculate_again == "y":
        continue
    # When user types "n", calculator stops
    elif calculate_again == "n":
        break
