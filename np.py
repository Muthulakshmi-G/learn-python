import numpy as np
#create function thet generates 10 integers and use it to buld an array# 
def generate():
    for x in range(10):
        yield x
Z=np.fromiter(generate(),float,count=-1)
print(Z)
#
Z=np.linspace(0,1,12,endpoint=True)[1:-1]
print(Z)

#..
def allnumbers():
    for i in range(10):
        print(i,i<8)
a=allnumbers()
print(a)
n=np.sum(allnumbers())
print(n)

#sorting
Z=np.random.random(100)
Z.sort()
print(Z)

#two random arrays check if they are qual
A=np.random.randint(0,2,5)
print(A)
B=np.random.randint(0,2,5)
print(B)
equal=np.array([A,B])
print(equal)



#is the following expression true?
np.sqrt(-1)==np.emath.sqrt(-1)

#how to get the dates of yesterday ,todat,tomorrow?

