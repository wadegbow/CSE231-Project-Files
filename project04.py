# Project 04

# set calculate_again so loop runs
calculate_again = 'yes'

# function to calculate tuition
def calculateTuition (resident, level, college, credit):
    # set taxes to be set later
    # only the fm_radio tax applies to all students
    asmsu = 0
    cogs = 0
    fm_radio = 3
    state_news = 0

    # check if the student is full time or part time
    # if the student has more than 6 credits, add the state_news fee
    if credit >= 6:
        time = 'full'
        state_news = 5
    elif credit > 4:
        time = 'full'
    elif credit > 0 and credit <= 4:
        time = 'part'

    # check to see if the student is an engineering graduate student
    # if not, check to see if they are just a graduate student
    # all graduate students have a cogs fee
    # if not, they are an undergraduate, add asmsu fee
    if level == 'graduate' and college == 'engineering':
        college = 'engineering graduate'
        cogs = 9.25
    elif level == 'graduate':
        college = 'graduate'
        cogs = 9.25
    else:
        asmsu = 18

    # per credit pricing structure
    per_credit = {
                        "lower":{"yes":440,"no":1165.50},
                        "upper":{"yes":490.25,"no":1202.25},
                        "graduate":{"yes":646.00,"no":1269.00}
                  }
    # per semester fee pricing structure
    per_semester = {
                        "none":{"part":0,"full":0},
                        "business":{"part":100,"full":200},
                        "engineering":{"part":361,"full":590},
                        "health":{"part":50,"full":100},
                        "sciences":{"part":50,"full":100},
                        "graduate":{"part":37.50,"full":75},
                        "engineering graduate":{"part":398.50,"full":665}
                    }


    # get the credit value from the dictionary, multiply by number of credits
    cost_credit = per_credit[level][resident]*credit
    # get the semester fee value from the dictionary
    cost_fees = per_semester[college][time]
    # calculate taxes by added them all together
    cost_taxes = asmsu+cogs+fm_radio+state_news

    # calulate total 
    total = cost_credit + cost_fees + cost_taxes

    # return total
    return float(total)


while calculate_again == 'yes':
    # set college to none, will be set later for upper level and graduates
    college = 'none'

    # prompt user for residency
    resident = input("Resident (Yes/No): ").lower()
    # prompt user for level
    level = input("Input level - freshman, sophomore, junior, senior, \
graduate: ").lower()

    # to simply things later,
    # freshman/sophomore = lower
    # junior/senior = upper
    # graduate = graduate
    if level == 'freshman' or level == 'sophomore':
        level = 'lower'
    elif level == 'junior' or level == 'senior':
        level = 'upper'
    elif level == 'graduate':
        level = 'graduate'

    # prompt upper and graduate level students to enter a college
    if level == 'upper' or level == 'graduate':
        college = input("College - business, engineering, health, sciences, \
None: ").lower()
    
    # get number of credits
    credit = float(input("Input credits this semester: "))

    # pass residency, level, college and credits through function
    # print the return value, format with commas, two decimals and a dollar sign
    print("Total Bill: ","${:#,.2f}".format(calculateTuition(resident, level, college, credit)))

    # ask the user if they want to calculate again
    calculate_again = input("\nDo you want to calculate again (Yes/No): ").lower()
    print()
