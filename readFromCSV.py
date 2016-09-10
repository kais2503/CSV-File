import csv
with open('file.csv') as csvfile:  # 'file.csv is the name of my csv file you should replace it by your csv file'
    delimiter=input('choose a delimiter') # in my case the delimiter is a comma
    readCSV=csv.reader(csvfile,delimiter= delimiter)
    Country=[]
    Language=[]
    Population=[]

    for row in readCSV:
        Country.append(row[0])
        Language.append(row[1])
        Population.append(row[2])

    print('Country=',Country)
    print('Language=',Language)
    print('Population=',Population)
