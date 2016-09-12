# Project 05 part b
# A program that opens a file based on user entered filename.
# Prompts the user for a year and region then finds each line
# that has an equal year and region. Using the result set calculate
# total population, average population, lowest population and highest.
# It will also count the number of records found.

# this function returns a file object
def open_file():
    filename = '' 

    # loop runs until the filename has a value
    while filename == '':
        # prompt the user for a filename
        filename = input('Enter the file to open: ')

        # try to open the file
        try:
            # open the file in read mode
            file = open(filename, 'r')
            # return the file object
            return file
        
        # check for FileNotFoundError
        except FileNotFoundError:
            print('No file with the name',filename,'exists.')
            # reset the filename so loop runs again
            filename = ''

        #check for eoferror
        except EOFError:
            print('\nKeyboard Interrupt. Ending program.')
            break 

# this function will process the file
def process_file(file):
    # set initial values
    search_year = ''
    search_region = ''
    total_pop = 0
    count = 0

    # put our prompts and calcs in a while loop so if the user
    # misenters a command we can prompt them again
    while search_year.lower() != 'quit':
        # check the year to make sure it wasn't a quit command or
        # too small of a number.
        try:
            # get a year input from the user
            search_year = input('Enter a year: ')
            
            if len(search_year) == 4 and int(search_year):
                # prompt the user to enter a region
                search_region = input('Enter a region: ')

                # the following block of if statements checks for valid
                # region codes while also formatting the leading statement
                # with full region names
                if search_region.lower() == 'afr':
                    lead = 'Report for Africa in'
                elif search_region.lower() == 'amr':
                    lead = 'Report for Americas in'
                elif search_region.lower() == 'sear':
                    lead = 'Report for South-East Asia in'
                elif search_region.lower() == 'eur':
                    lead = 'Report for Europe in'
                elif search_region.lower() == 'emr':
                    lead = 'Report for Eastern Mediterranean in'
                elif search_region.lower() == 'wpr':
                    lead = 'Report for Western Pacific in'
                else:
                    # if the code was invalid, tell the user and start over
                    print('The region code was invalid.')
                    continue

                # this for loop searches the file and calculates the report
                for line in file:
                    # set our variables with data from the file
                    year = str(line[0:4])
                    country = str(line[5:55]).rstrip()
                    region = str(line[56:60]).strip()
                    population = int(line[62:72])

                    # check to see if our search terms match the
                    # variables we set above
                    if search_year == year and \
                       search_region.lower() == region.lower():
                        # first time through the loop set lowest and greatest
                        if count == 0:
                            low_pop = population
                            low_country = country
                            great_pop = population
                            great_country = country
                        # each time compare new value to last greatest
                        if population > great_pop:
                            great_pop = population
                            great_country = country
                        # each time compare new value to last lowest
                        if population < low_pop:
                            low_pop = population
                            low_country = country
                        # add the population to total_pop
                        total_pop += population
                        # increment the count
                        count += 1
                
                print() # add whitespace
                print(lead,search_year+':') # print leading statement
                print(count,'records were found.') # print count

                # if records were found
                if count > 0:
                    # print total population
                    print('The total population is:',
                          "{:#,}".format(total_pop*1000))
                    # print average population
                    print('The average population is:',
                          "{:#,}".format(int(total_pop*1000/count)))
                    # print smallest population
                    print('The smallest country',low_country+':',
                          "{:#,}".format(low_pop*1000))
                    # print largest population
                    print('The largest country',great_country+':',
                          "{:#,}".format(great_pop*1000))
                break # exit the loop
            
            else:
                # this else fires when the year entry is invalid
                print('Year was invalid. Make sure to enter a 4 digit year.')
                # start the loop over
                continue

        # if the search year cant be converted to an integer
        except ValueError:
            # check if the non integer value was quit
            if search_year.lower() == 'quit':
                print('Quitting the program.')
                break # exit the loop
            else:
                print('Year was invalid. Make sure to enter a 4 digit year.')
                # start the loop over
                continue

        #check for eoferror
        except EOFError:
            print('\nKeyboard Interrupt. Ending program.')
            break
            

# main function calls open_file() and process_file()
# and closes the file returned from open_file()
def main():
    try:
        file = open_file()
        process_file(file)
        file.close()

    except EOFError:
        print('\nKeyboard Interrupt. Ending program.')

# call the main function to get things started
main()
        
    
    
