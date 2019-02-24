import csv

#Create new file
f= open("dataset_modified.csv","w+")

#delimiterToReplace
delimiterToReplace = "|||"

#Open file
with open('dataset.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #counter of rows
    c = 0

    for row in readCSV:
        r = str(row)

        #replace thing in file to make more columns
        row_string = r.replace(delimiterToReplace, ",")

        #count number of columns generated
        column_count = row_string.count(",")

        #write new row into new file
        f.write(row_string+"\n")
        
        print("Row: "+str(c)+" - Columns: "+str(column_count))

        c+=1

f.close()
