# set the constant values
# current population based on given statistic
current_pop = int(318651218)
# seconds in a year calculated by 365days*24hours*60minutes*60seconds
seconds_in_year = 365*24*60*60

# explain the program
print("Predict the future population of the United States.")

# get the user input for years
yrs_str = input("Input the number of years in the future"\
                "for the prediction: ")

# convert the input string to an integer
yrs_int = int(yrs_str)

# convert the years inputted into seconds by multiplying by our constant
seconds_int = yrs_int*seconds_in_year

# take total seconds and divide by 7 (1 birth every 7 sec)
births = seconds_int//7

# take total seconds and divide by 13 (1 death every 13 sec)
deaths = seconds_int//13

# take total seconds and divide by 40 (1 immigrant every 40 sec)
immigrants = seconds_int//40

# using the total births, deaths and immigrants we calculate the gross change
gross_change = (births + immigrants) - deaths

# form a prediction by adding the gross change to the current population
prediction = current_pop + gross_change

# print the result
print("New population in ",yrs_int," years will change by " \
      ,gross_change," to be ",prediction)
