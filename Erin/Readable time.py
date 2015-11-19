import time
import datetime
filename = "Day1-20150720095910.csv"
file = open("Day1note4.txt", "w")
with open(filename) as f:
    linenumb = 0
    for line in f:
        linenumb = linenumb+1
        if linenumb == 1:
            file.write("Date")
            file.write(",")
            file.write(line)
            continue
        stripline = line.strip()
        columns = stripline.split(',')
        print columns[0]
        my_variable = time.localtime(int(columns[0]))
        str = time.asctime(my_variable)
        file.write(str)
        file.write(",")
        file.write(stripline)
        file.write("\n")
file.close()
