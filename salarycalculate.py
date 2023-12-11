#Pre-determined Values
monthly_basic_salary = 3800000
hourly_overtime_pay = 110000
level_1_allowance = (5 * monthly_basic_salary)/100
level_2_allowance = (10 * monthly_basic_salary)/100
level_3_allowance = (15 * monthly_basic_salary)/100

#Initial Message
while True:
    print(f"Welcome to the Overtime Salary Calculator!")
    print(f"The base monthly salary is: ${monthly_basic_salary:,}")
    print(f"The hourly overtime rate is: ${hourly_overtime_pay:,}")
    #User Input
    while True:
        try:
            hours_worked = float(input("Enter the number of overtime hours worked (0-20 hours): "))
            hours = hours_worked
            if hours > 20 or hours < 0:
                print("Invalid number of hours! Please try again.")
                continue
            else:
                break
        except ValueError:
            print ("Invalid Entry, Please enter a numeric value")
        continue

    while True:
        allowance_level = input("Please enter the allowance level (1/2/3): ")
        if allowance_level == "1":
            allowance_percent = level_1_allowance
            break
        elif allowance_level == "2":
            allowance_percent = level_2_allowance
            break
        elif allowance_level == "3":
            allowance_percent = level_3_allowance
            break
        else:
            print ("Invalid Entry, please choose from 1 to 3.")
            continue

    #Calculations
    total_salary = monthly_basic_salary + (hourly_overtime_pay * hours_worked) + (allowance_percent)

    print(f"The total earned salary with {hours_worked} hours of overtime and a Level {allowance_level} Allowance is ${total_salary:,}")
    print("")
    process = input(f"Would you like to calculate again? [Y/N]: ").lower()
    while True:
        if process != 'y' and process != 'n':
            process = input("Invalid response. Enter Y or N: ").lower()
        else:
            break
    if process == "y":
        print("---------------------------------------------------------------------------------------------------")
        continue
    elif process == "n":
        break
        
