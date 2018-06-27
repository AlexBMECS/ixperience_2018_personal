# -*- coding: utf-8 -*-
"""
In this example we are going to build an application that reads the most popular names
in the US, taken from the Social Security Administration's site:

https://www.ssa.gov/oact/babynames/

This application will have the following functionalities:

- It will accept a name as an argument
- It will read a list of files (located in the folder data). Each file contains the
most popular baby names for boys and girls for a certain year (the year is in the filename)
- For the name provided as an argument, print out how many years it's been among the most popular among boys and girls
"""
year  = 1900
big_data =  []
for i in range(117):

	data = "data/names_" + str(year)+".txt"
	file_name = open(data, 'r')

	line = content.split("|")

	big_data.append(line[1])
	big_data.append(line[2][:-1])

	year+=1

num = [big_data.count(i) for i in big_data]

final = [y for y in sorted(set(zip(num,big_data)))]

print(final)


    
