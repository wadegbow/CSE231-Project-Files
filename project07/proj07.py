# Project 07
# Calculate average change in GDP for presidential terms.

# this function gets all the gdp data from
# csv files and adds them to a list
def get_gdp():
    # initialize lists
    years = []
    gdp = []
    year_gdp = []

    # try to open .csv data files
    try:
        file1 = open('GDP_Section1All_Hist1.csv', 'r')
        file2 = open('GDP_Section1All_Hist2.csv', 'r')

        # get lines from each .csv file
        f1_lines = file1.readlines()[7:9]
        f2_lines = file2.readlines()[7:9]

        # split all of the lines at each comma
        f1_line8 = f1_lines[0].split(',')
        f1_line9 = f1_lines[1].split(',')
        f2_line8 = f2_lines[0].split(',')
        f2_line9 = f2_lines[1].split(',')        

        # append all years from first file
        i = 0
        for x in f1_line8:
            if i > 2:
                if x != '' and x != '\n':
                    years.append(int(x))
            i+=1

        # append all years from second file
        i = 0
        for x in f2_line8:
            if i > 3:
                if x != '' and x != '\n':
                    years.append(int(x))
            i+=1

        # append all gdp from first file
        i = 0
        for x in f1_line9:
            if i > 2:
                if x != '' and x != '\n':
                    gdp.append(x)
            i+=1

        # append all gdp from second file
        i = 0
        for x in f2_line9:
            if i > 3:
                if x != '' and x != '\n':
                    gdp.append(x)
            i+=1

        # combine year and gdp lists
        i = 0
        for year in years:
            tmp = (years[i], gdp[i])
            year_gdp.append(tmp)
            i+=1

        # return the combined list
        return year_gdp
            
    # handle FileNotFoundError if files dont exist
    except FileNotFoundError:
        print('Make sure GDP_Section1All_Hist1.csv and \
              GDP_Section1All_Hist2.csv exist in this folder.')


# this function gets the presidents name, years in office
# and their party then adds them to a list
def get_presidents():
    # initialize list
    presidents = []

    # try to open presidents file
    try:
        file = open('presidents.txt','r')

        # get all lines, skipping the first
        lines = file.readlines()[1:]

        # this for loop builds the presidents list
        for line in lines:
            # split each line at commas
            tmp = line.split(',')

            # check for an extra field, remove it with pop
            # this handles the jr in carters name
            if len(tmp) > 3:
                tmp.pop(1)

            # check if it was a split term
            # if yes, combine names
            if '+' in tmp[0]:
                names = tmp[0].split('+')
                last_name = names[0].split(' ')[2] + '-' + \
                            names[1].lstrip().split(' ')[2]
            else:
                last_name = tmp[0].split(' ')[-1]

            # convert the years as president into a list
            years_worked = tmp[1].strip().split('-')
            years_worked = list(range(int(years_worked[0]),\
                                      int(years_worked[1])))

            party = tmp[2].lstrip()[:-1]

            # check if the president served one term
            if len(years_worked) == 4:
                presidents.append((last_name,years_worked,party))
            # or if he served two terms, append two records
            elif len(years_worked) == 8:
                presidents.append((last_name+'1',years_worked[0:4],party))
                presidents.append((last_name+'2',years_worked[4:9],party))

        # return the presidents list
        return presidents

    # if the file is not found, inform the user
    except FileNotFoundError:
        print('File not found.')


# this function takes a list of years and gdp and a list
# of years and presidents and calculates the average gdp
# for each term
def calculate_average_gdp(year_gdp, presidents):

    calculated_list = []

    # loop through presidents
    for x in presidents:
        term_gdp = 0
        count = 0
        party = x[2]
        # loop through years in presidents
        for y in x[1]:
            # loop through year in year_gdp
            # compare terms, sum gdp
            for year, gdp in year_gdp:
                if year == y:
                    term_gdp += float(gdp)
            
            count+=1

        # append name, rounded average gdp, and party
        calculated_list.append((x[0], round(term_gdp/count,1), x[2]))

    # return the calculated list
    return calculated_list


# this list takes the calculated list and displays it
# with the proper formatting
def display_list(calculated_list):

    # initialize values
    total_gdp_dem = 0
    total_gdp_rep = 0
    total_count_dem = 0
    total_count_rep = 0

    # setup a format template
    format_template = "{0:>15}  {1:>6}  {2:<7}"

    # print header
    print('GDP Growth by Presidential Term')
    print()

    # loop through items in the calculated list
    for item in calculated_list:
        gdp = '('+str(item[1])+'):'

        # total democratic gdp
        if item[2].lower() == 'democrat':
            total_gdp_dem += item[1]
            total_count_dem += 1

        # total republican gdp
        elif item[2].lower() == 'republican':
            total_gdp_rep += item[1]
            total_count_rep += 1

        # print the presidential gdp with formatting
        print(format_template.format(item[0], gdp, item[2][0]*round(item[1])))

    # calculate democrat avg and republican avg
    dem_avg = total_gdp_dem/total_count_dem
    rep_avg = total_gdp_rep/total_count_rep

    # print whitespace and party averages
    print()
    print(format_template.format('Democrat', '('+str(round(dem_avg,1))+'):', \
                                 'D'*round(dem_avg)))
    print(format_template.format('Republican', '('+str(round(rep_avg,1))+'):', \
                                 'R'*round(rep_avg)))

# this function runs all the previous functions           
def main():
    display_list(calculate_average_gdp(get_gdp(),get_presidents()))
    
main()