# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:43:35 2021

@author: psnma
"""

import csv

#Open and read csv file

#Open and reading csv file as a list
with open('username.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile,dialect='excel', delimiter=';')
    
# =============================================================================
#     #printing rows
#     for row in csvReader:
#         print(row)
# =============================================================================
    for row in csvReader:
        for value in row:
            print(value,end=" ")
        print("\n")
        
#Open and reading csv file as a dictionary
with open('username.csv','r') as csvfile:
    csvReader = csv.DictReader(csvfile, delimiter = ";")    
    
    for row in csvReader:
        for key in row.keys():
            print(key, row[key])
            
            
#Save data to csv file:

#Saving line by line
with open('example_file1.csv', 'w', encoding='utf-8', newline='') as csvfile:
    # initial "writer"
    csvWriter = csv.writer(csvfile)
    # seting column names
    csvWriter.writerow(['Name', 'Surname', 'Age'])
    # rows with values
    csvWriter.writerow(['Simon', 'Chomej', '37'])
    csvWriter.writerow(['Agnes', 'Bunch', '25'])
    csvWriter.writerow(['John', 'Doe', '44'])
    
#Saving struct
struct = {'Name': 'Simon',
          'Surname': 'Chomej',
          'Age': '37',
          'City': 'Olsztyn'}

struct2 = {'Name': 'Nicole',
           'Surname': 'Jordan',
           'Age': '29'}

struct3 = {'Name': 'Richard',
           'Surname': 'Johnson',
           'Age': '54',
           'City': 'New York'}

structList = [struct, struct2, struct3]

with open('example_file2.csv', 'w', encoding='utf-8', newline='') as csvfile:
    # define and save column names
    fieldNames = ['Name', 'Surname', 'Age', 'City']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldNames)
    csvwriter.writeheader()

    # saving struct
    for n in structList:
        csvwriter.writerow(n)
    
    
    
    
    
    
    
    