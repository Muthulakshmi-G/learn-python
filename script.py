import csv
import numpy as np
with open("winequality-red.csv",'r') as csvfile:
    wines=list(csv.reader(csvfile,delimiter=","))
    for row in wines:
        print(','.join(row))

empty_array=np.zeros((3,4))
print(empty_array)

#a=np.random.rand(3,4)
#print(a)


#print(wines[2,3])
