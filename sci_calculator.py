import math

calc_start = True
calc_num = 0
answer = 0.0
# Intial loop to start calculator
while calc_start:
    print(f"Current Result: {answer}")

    print(" Calculator Menu ")
    print(" --------------- ")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average\n")
    menu_choice = int(input("Enter Menu Selection:"))
    print(" ")

    if menu_choice == 7:
        print("Error: No calculations yet to average!")
        menu_choice = int(input("Enter Menu Selection:"))

    if menu_choice == 0:
        print("Thanks for using this calculator. Goodbye!")
        calc_continue = False
        calc_start = False
        break

    #Number is outside of Menu
    if menu_choice > 7:
        print("Error: Invalid selection!")
        menu_choice = int(input("Enter Menu Selection:"))

    elif menu_choice < 0:
        print("Error: Invalid selection!")
        menu_choice = int(input("Enter Menu Selection:"))

    if menu_choice == 0:
        print("Thanks for using this calculator. Goodbye!")
        calc_continue = False
        calc_start = False
        break



    first_operand = float(input("Enter first operand:"))
    second_operand = float(input("Enter second operand:"))
    total_average = 0



    if menu_choice == 1:
        answer = first_operand + second_operand
        print(f"Current Result: {answer}")
        total_average += answer
        calc_num += 1

    elif menu_choice == 2:
        answer = first_operand - second_operand
        print(f"Current Result: {answer}")
        total_average += answer
        calc_num += 1

    elif menu_choice == 3:
        answer = first_operand * second_operand
        print(f"Current Result: {answer}")
        total_average += answer
        calc_num += 1

    elif menu_choice == 4:
        answer = first_operand / second_operand
        print(f"Current Result: {answer}")
        total_average += answer
        calc_num += 1

    elif menu_choice == 5:
        answer = first_operand ** second_operand
        print(f"Current Result: {answer}")
        total_average += answer
        calc_num += 1

    elif menu_choice == 6:
        answer = math.log(second_operand, first_operand)
        print(f"Current Result: {answer}")
        total_average += answer
        calc_num += 1

    # Keep asking user if they want to user calculator
    calc_continue = True

    while calc_continue:

        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average\n")
        menu_choice = int(input("Enter Menu Selection:"))
        print(" ")

        if menu_choice == 7:
            average = total_average / calc_num
            average = round(average, 2)
            print(f"Sum of calculations:{total_average} ")
            print(f"Number of calculations:{calc_num}")
            print(f"Average of calculations:{average}")
            menu_choice = int(input("Enter Menu Selection:"))

        if menu_choice == 0:
            print("Thanks for using this calculator. Goodbye!")
            calc_continue = False
            calc_start = False
            break

        # else:
        # print("Error: Invalid selection!")

        first_operand = float(input("Enter first operand:"))
        second_operand = float(input("Enter second operand:"))

        if menu_choice == 1:
            answer = first_operand + second_operand
            print(f"Current Result: {answer}")
            calc_num += 1
            total_average += answer

        elif menu_choice == 2:
            answer = first_operand - second_operand
            print(f"Current Result: {answer}")
            calc_num += 1
            total_average += answer

        elif menu_choice == 3:
            answer = first_operand * second_operand
            print(f"Current Result: {answer}")
            calc_num += 1
            total_average += answer

        elif menu_choice == 4:
            answer = first_operand / second_operand
            print(f"Current Result: {answer}")
            calc_num += 1
            total_average += answer

        elif menu_choice == 5:
            answer = first_operand ** second_operand
            print(f"Current Result: {answer}")
            calc_num += 1
            total_average += answer

        elif menu_choice == 6:
            answer = math.log(second_operand, first_operand)
            print(f"Current Result: {answer}")
            calc_num += 1
            total_average += answer
