
#we usually use 
x=[1,2,3,4]
out=[]
for  item in x:
    out.append(item**2)
print(out)

#list comprehension makes easy
y=[1,2,3,4]
out1=[item**2 for item in y]
print(out1)


#lamda functions

double=lambda x:x*2
print(double(5))

#map function
seq=[1,2,3,4,5]
result=list(map(lambda var:var*2,seq))
print(result)

def mul(x):
    return x*x
def add(x):
    return x+x


func=[mul,add]
for i in range(5):
    values=list(map(lambda x: x(i),func))
    print(values)


#filter
num=[1,2,3,4,5]
result1=list(filter(lambda x:x>2,num))
print(result1)

