# Project 08
# process files using dictionaries and functions

def format_result(row):
    """
    This function accepts both user_search results and min_max
    results, formats them, then prints them.
    """
    
    format_template = "{0:>11} = {1:<20}" # template for formatting

    # population and births are converted to integers
    population = int(row['POPESTIMATE2013'])
    births = int(row['BIRTHS2013'])

    # each line is printed using the template so things are aligned
    print(format_template.format('State name', row['STNAME']))
    print(format_template.format('County name', row['CTYNAME']))
    print(format_template.format('PopEst', "{:,}".format(population)))
    print(format_template.format('Births', "{:,}".format(births)))
    print(format_template.format('NetMigr', \
                                 round(float(row['RNETMIG2013']),2)))
    print()

def user_search(census_data):
    """
    This function uses census_data and user inputs to search
    for a specific location's data. It runs format_result.
    """
    
    county = 'init'
    state = ''

    # while loop that prompts the user for inputs
    # if statements are used to stop the loop when q or quit
    # is entered 
    while county:
        state = input("Which state or q/quit to halt: ")
        if state.lower() == 'q' or state.lower() == 'quit':
            break
        county = input("Which county or q/quit to halt: ")
        if county.lower() == 'q' or county.lower() == 'quit':
            break
    
        row = (state.lower(), county.lower())

        format_result(find_data(census_data, row))
        

def find_data(census_data, row):
    """
    This function uses a tuple containing state and county
    to search census_data for the full data set. The full data
    set is returned.
    """

    if census_data[row]:
        return census_data[row]

def census_min_max(census_data):
    """
    This function calculates the minimum and maxium
    county populations. Both min and max are returned.
    """

    i = 0
    # this loop calculates the minimum and maximum locations
    for row in census_data:
        if row[0] == row[1]:
            continue
        
        population = float(census_data[row]['POPESTIMATE2013'])
        
        if i == 0:
            low_pop = population
            low_row = row
            high_pop = population
            high_row = row
        if population > high_pop:
            high_pop = population
            high_row = row
        if population < low_pop:
            low_pop = population
            low_row = row
        i+=1

    return high_row, low_row
                               
def build_census_data(file):
    """
    This function builds and returns dictionary using all of the
    relevant data from the csv file.
    """

    relevant_headers = ['CTYNAME','STNAME','POPESTIMATE2013','BIRTHS2013', \
                        'RNETMIG2013']
    search_key = {}
    file_list = []
    census_data = {}

    # this loop creates a list from the data in file
    for line in file:
        file_list.append(line.strip().split(','))

    
    i = 0
    # this loop builds a search key for use in the next loop
    for header in file_list[0]:
        if header in relevant_headers:
            search_key[header] = i
        i+=1

    i = 0
    # two loops are used to get only relevant values
    # for populating the census_data dictionary
    for line in file_list[1:]:
        tmp_dict = {}
        for k,v in search_key.items():
            tmp_dict[k] = line[v]
        census_data[(tmp_dict['STNAME'].lower(),\
                     tmp_dict['CTYNAME'].lower())] = tmp_dict
        i+=1

    return census_data
        

def open_file():
    """
    This function will try to open a csv file and return it.
    If the file is not available it will halt the program.
    """
    try:
        file = open( "CO-EST2013-Alldata.csv", "r", encoding ="ISO-8859-1" )

    except FileNotFoundError:
        print('Data file not found.')

    return file

def main():
    """
    This function is used to start the program. 
    """
    
    file = open_file() # open the csv file

    census_data = build_census_data(file) # use the file to build data

    min_max = census_min_max(census_data) # find min and max sets

    # print max results
    print('County with largest population:')
    format_result(find_data(census_data, min_max[0]))

    # print min results
    print('County with smallest population:')
    format_result(find_data(census_data, min_max[1]))

    # allow user to search for a specific location
    user_search(census_data)
    

main()
    
