import math
#method 1
def area(r):

    return math.pi*(r**2)

radii=[2,5,7.1,0.3,10]

areas=[]
for r in radii:
    a=area(r)
    areas.append(a)

print(areas)

#method2
print(map(area,radii))#it gives map object
print(list(map(area,radii)))#it gives list of area of values



def area_of_rec_prism(a,b,c):
    
    return 2*a*b+2*b*c+2*a*c
values=[a:10,b:20,c:30,a1:40,b1:50,c1:60]
area1=area_of_rec_prism(values)
print("the prism area is",area1)

print(map(area_of_rec_prism,values))


