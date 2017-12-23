class Point:
    """ point class represents and manipulates x,y coords"""
    def __init__(self):
        """create a new point at the origin"""
        self.x=0
        self.y=0

p=Point()
q=Point()

print(p.x,p.y,q.x,q.y)



p.x=3
p.y=4
x=p.x
y=p.y
print(p.y)
print(p.x)

print("(x={0},y={1})".format(p.x,p.y))
distance_squared_from_origin=p.x*p.x+p.y*p.y
print(distance_squared_from_origin)

#to create point 7,6 now we need

p=Point()
p.x=7
p.y=6
#now we make class constructor more general by placing extra parameter in to __init__method

class Point:
    """point class represents and manipulates x,y coords"""
    def __init__(self,x=0,y=0):
        """create a new point at x,y"""
        self.x=x
        self.y=y
p = Point(4, 2)
q = Point(6, 3)
r = Point()       # r represents the origin (0, 0)
print(p.x, q.y, r.x)

def distance_from_origin(self): 
        print(((self.x**2)+(self.y**2))**0.5)



p=Point()
print(p.x) 
print(p.y) 


print(p.distance_from_origin())

                                                                   
