# Project 05 part a

# initialize variables
user_input = ''
user_filename = ''

# if the filename is blank, prompt user for one
if user_filename == '':
    user_filename = input('Enter a filename: ')

# use with to open both the input and output files
with open('population.txt', 'r') as file, open(user_filename, 'w') as user_file:       

    # prompt the user to enter a year
    user_input = input('Enter a year: ')

    # check to see if the year is all or blank
    if user_input.lower() == 'all' or user_input == '':
        # use a for loop to write each line to output file
        for line in file:
            # print(line)
            user_file.write(str(line))
    else:
        # use a for loop to write each found line to the output file
        for line in file:
            # get the year
            year = str(line[0:4])
            # check if the year contains our search term
            # use slicing to check partial searches
            if user_input == year[:len(user_input)]:
                # print(str(line))
                user_file.write(str(line))

    # close file to save
    user_file.close()
