'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 8 Yearly Precipitation

This program is run through the command line.
'''

'''
thing = data["Portland"]["2010"]
hardcode files
t.exitonclick()
'''

# input city name
# get snow data
# figure out how to print the # of skips into the outpudata data file 
# file_out.write(errorfunc(i-2010))
# portland_data[year - 2010].append(float(line_list[9]))

#read returns as a string
#readlines returns as a list

from operator import contains
import sys
import os
import shlex

def read_in(input_file):
    file_in = open(input_file,"r")
    input_contents = file_in.read().replace('"','')
    file_in.close()
    #print(input_contents)
    #print(type(input_contents))
    #print(input_contents[1])s
    #print(input_contents[160])
    #input_list = input_contents.split('')
    #print(input_list)
    #for i in input_contents:
    for line in input_contents.splitlines():
        line_list = line.split(',')
        #print(line_list)
        if line_list[1].startswith("PORTLAND"):
            print(line_list)
        #print(line)
        #print((type(input_contents)))
        #print(line[0])
        #print(input_contents[i])
        #print(len(input_contents[i])
        #print(input_list)
        #final_list = input_list[i].replace('"','')
        #print(input_list)

#def read_in(input_file):
    #file_in = open(input_file,"r")
    #input_contents = file_in.readlines() 
    #file_in.close()
    #for i in range(len(input_contents)):
        #print(input_contents[i])
        #sub_list = shlex.split(input_contents[i])
        #print(sub_list)
        #print(len(sub_list))
        #print(type(sub_list))
        #for j in range(len(sub_list)):
            #sub_sub_list = sub_list[j].split(',')
            #if sub_sub_list[1].startswith("PORTLAND"):
            #if "PORTLAND" in sub_sub_list[1]:
                #print(sub_sub_list)
    #for i in range(len(input_contents)):
        #print(len(input_contents[i]))
        #input_list = input_contents[i].split(',')
        #final_list = input_list[i].replace('"','')
        #print(final_list)
        #for j in range(len(input_list)):
           #final_list = input_list[j].replace('"','')
           #print(''.join(final_list))
        #for j in input_list
        #final_list = input_list[i].replace('"','')
        #print(input_list)
        #print(final_list)
        #if "PORTLAND" in input_list[1]:
        #if input_list[1].startswith('"PORTLAND'):
            #print(input_list)'''

def usg_msg():
    print("Welcome to the program.")

def menu():

    try:

        input_file = input("Enter the exact name of the .csv data file you'd like to work with:\n")

        # Checks that the input file is a .csv file.
        if (input_file.endswith(".csv") == False):
            raise ValueError("Input file must be a .csv file.")

        # Checks that the file exists.
        elif (os.path.exists(input_file) == False):
            raise OSError("Input file does not exist.")

        else:

            output_file = input("Enter the exact name of the .csv file where you'd like to print the data:\n")
            
            # Checks that the onput file is a .csv file.
            if (output_file.endswith(".csv") == False):
                raise ValueError("Output file must be a .csv file.")

            elif (os.path.exists(output_file) == False):
                raise OSError("Output file does not exist.")

            else:
                usg_msg()
                read_in(input_file)

    # Error raised when there are an incorrect number of arguments.
    except OSError as ose:
        print(ose)

    # Error raised when the input file is not a .csv file.
    except ValueError as ve:
        print(ve)
    

def main():
    menu()
    
main()

'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 8 Yearly Precipitation
'''

from operator import contains
import os

def translateLine(list_to_append_to, line_to_make_float, year, times_error_block_hit):
    try:
        list_to_append_to.append(float(line_to_make_float))
    except:
        times_error_block_hit += 1
        #print("I failed in debugging " + year)
        #print("Failed to translate line to float, probably because it is an empty value")

def read_in(input_file):
    times_error_block_hit = 0
    file_in = open(input_file,"r") #look at this file
    input_contents = file_in.read().replace('"','') #read in content, remove quotes
    file_in.close() #close file to save memory
    portland_data = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for line in input_contents.splitlines(): #splits string at the line breaks into the list
        line_list = line.split(',') #creates a list of each line with the , as the deliminator
        if line_list[1].startswith("PORTLAND"): #if the second list item starts with PORTLAND
            date = line_list[3].split('-') #creates another sub list within the fourth list item, splits by - 
            year = date[0]
            if year == "2010":
                try:
                    portland_data[0].append(float(line_list[9]))
                except:
                    times_error_block_hit += 1
                #translateLine(portland_data[0], line_list[9], "2010", times_error_block_hit)
            '''elif year == "2011":
                translateLine(portland_data[1], line_list[9], "2011", times_error_block_hit)
                # portland_data[1].append(float(line_list[9]))
            elif year == "2012":
                print("HEY IDIOT I'M IN 2012, here is the value")
                portland_data[2].append(float(line_list[9]))
            elif year == "2013":
                print("HEY IDIOT I'M IN 2013, here is the value")
                portland_data[3].append(float(line_list[9]))
            elif year == "2014":
                print("HEY IDIOT I'M IN 2014, here is the value")
                portland_data[4].append(float(line_list[9]))
            elif year == "2015":
                print("HEY IDIOT I'M IN 2015, here is the value")
                portland_data[5].append(float(line_list[9]))
            elif year == "2016":
                print("HEY IDIOT I'M IN 2016, here is the value")
                portland_data[6].append(float(line_list[9]))
            elif year == "2017":
                print("HEY IDIOT I'M IN 2017, here is the value")
                portland_data[7].append(float(line_list[9]))
            elif year == "2018":
                print("HEY IDIOT I'M IN 2018, here is the value")
                portland_data[8].append(float(line_list[9]))
            elif year == "2019":
                print("HEY IDIOT I'M IN 2019, here is the value")
                portland_data[9].append(float(line_list[9]))
            elif year == "2020":
                print("HEY IDIOT I'M IN 2020, here is the value")
                portland_data[10].append(float(line_list[9]))
            elif year == "2021":
                print("HEY IDIOT I'M IN 2021, here is the value")
                portland_data[11].append(float(line_list[9]))'''
    print(portland_data[0])
    print("Below will tell you how many errors you've hit")
    print(times_error_block_hit)
                
def read_out(input_data,output_file):
    file_out = open(output_file,"w") 
    file_out.writelines(input_data)
    file_out.close()

def usg_msg():
    print("Welcome to the program.")

def menu():

    try:

        input_file = input("Enter the exact name of the .csv data file you'd like to work with:\n")

        # Checks that the input file is a .csv file.
        if (input_file.endswith(".csv") == False):
            raise ValueError("Input file must be a .csv file.")

        # Checks that the file exists.
        elif (os.path.exists(input_file) == False):
            raise OSError("Input file does not exist.")

        else:

            output_file = input("Enter the exact name of the .csv file where you'd like to print the data:\n")
            
            # Checks that the onput file is a .csv file.
            if (output_file.endswith(".csv") == False):
                raise ValueError("Output file must be a .csv file.")

            elif (os.path.exists(output_file) == False):
                raise OSError("Output file does not exist.")

            else:
                usg_msg()
                read_in(input_file)

    # Error raised when there are an incorrect number of arguments.
    except OSError as ose:
        print(ose)

    # Error raised when the input file is not a .csv file.
    except ValueError as ve:
        print(ve)
    
def main():
    menu()
    
main()