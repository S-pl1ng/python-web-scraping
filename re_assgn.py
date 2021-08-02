#This assignment involves using Regular Expressions (RegEx) to extract and sum all numbers from a given file

import re

file = open(r"C:\Users\Hp\python_web_course\actual_data.txt")
total=0
for line in file:
    line=line.rstrip()
    num_list = re.findall("[0-9]+", line)
    if len(num_list)>0:
        for i in range(len(num_list)):
            total+=int(num_list[i])
print("Total sum is: ", total)
