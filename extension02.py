'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 8 Yearly Precipitation

Extension number 2 shows data for snowfall.
'''

from operator import contains
import os

'''
Function that reads in data from a .csv file, converts it to a list, and filters it by city/year
Parameters: .csv file
Returning: a list of lists
'''
def read_in(input_file,city_name):

    # Creates the City List 
    city_data = [[],[],[],[],[],[],[],[],[],[],[],[]]

    # Creates a list to store the year for each time the empty data field error block is hit
    error_hit_list = []

    # Sets the input file
    file_in = open(input_file,"r")

    # Reads in the input file as one big string, replaces the quoatation marks with nothing
    input_contents = file_in.read().replace('"','')

    # Close file to save memory
    file_in.close()

    # Creates a list, line by line, of the input data
    for line in input_contents.splitlines(): 

        # Splits each line into a sub list, separating items by the comma 
        line_list = line.split(',') 

        # If list index[1] starts with "city name", continue
        if line_list[1].startswith(str(city_name)): 

            # Splits the date list item into a second sub list, split by a hyphen
            date = line_list[3].split('-') 

            # Creates a variable equal to the first item in the date sub list
            year = date[0]

            # Goes through each year, adds year 2010 to city_data[0], year 2011 to city_data[1], and so on
            # If an error occurs, add the year to the error block list
            try:
                city_data[int(year) - 2010].append(float(line_list[10]))
            except:
                error_hit_list.append(year)
    
    # Prints the number of times the error block was hit (printed in terminal) 
    print("Number of days with no snow data per year:")
    for i in range(2010,2022,1):
        print("..." + str(i) + " : " + str(error_hit_list.count(str(i))))

    # Saves the portland_data list for later use
    return city_data

'''
Function that finds the average for a list
Parameters: a list, an integer
Returning: a float value, rounded to three decimal places
'''
def get_avgs(list_name,list_num):

    # Throws an error if argument one is not a list
    if type(list_name) != list:
        raise TypeError("Argument one for get_avgs needs to be a list.")
    
    # Throws an error if argument two is not an integer
    if type(list_num) != int:
        raise TypeError("Argument two for get_avgs needs to be a integer.")

    # The length of the list is the number of days
    number_of_days = len(list_name[list_num])

    # Gets sum of perciptation for a sent list
    sum_of_percipitation = sum(list_name[list_num])

    # Gets average 
    try:
        list_average = sum_of_percipitation/number_of_days

        # Saves result for later use, stores it as a float with three decimal places
        return f'{list_average:.3f}'

    # If there is no data for that year, print a statement to the terminal instead of getting the average.
    except:
        print("No data for year " + str(list_num + 2010))

'''
Function that prints a list of dates and averages in a new .csv file
Parameters: a list, a string, an integer, and a string
Returning: a .csv file presenting the data averages and years
'''
def print_avgs(data, city, starting_year, out_file):
    # Throws an error if the first argument is not a list
    if type(data) != list:
        raise TypeError("First argument in print_avgs is not a list.")

    # Throws an error if the second argument is not a string
    elif type(city) != str:
        raise TypeError("Second argument in print_avgs is not a string.")
    
    # Throws an error if the third argument is not an integer
    elif type(starting_year) != int:
        raise TypeError("Third argument in print_avgs is not a integer.")
    
    # Throws an error if the fourth argument is not a string
    elif type(out_file) != str:
        raise TypeError("Fourth argument in print_avgs is not a string.")

    # If all arguments are good, proceed to the final step in the program
    # Write data in the output file by looping through 2010-2021 and getting the average for every line in portland_data
    else:
        file_out = open(out_file,"w") 
        file_out.write(city.capitalize() + " Average Snowfall per Year:\n\n")
        for i in range(starting_year,2022,1):
            file_out.write(str(i) + " : " + str(get_avgs(data,(i - 2010))) + "\n")
            i += 1
        file_out.close()
    
def main():
    try:

        input_file = input("Enter the exact name of the .csv data file you'd like to work with:\n")

        # Checks that the input file is a .csv file.
        if (input_file.endswith(".csv") == False):
            raise ValueError("Input file must be a .csv file.")

        # Checks that the input file exists.
        elif (os.path.exists(input_file) == False):
            raise OSError("Input file does not exist.")

        else:

            output_file = input("Enter the exact name of the .csv file where you'd like to print the data:\n")
            
            # Checks that the output file is a .csv file.
            if (output_file.endswith(".csv") == False):
                raise ValueError("Output file must be a .csv file.")

            # Checks that the output file exists.
            elif (os.path.exists(output_file) == False):
                raise OSError("Output file does not exist.")

            else:
                city_name = input("What city would you like to get data for?\n")
                print_avgs(read_in(input_file,city_name.upper()),str(city_name),2010,output_file)
                
    # Error raised when there are an incorrect number of arguments.
    except OSError as ose:
        print(ose)

    # Error raised when the input file is not a .csv file.
    except ValueError as ve:
        print(ve)
    
main()