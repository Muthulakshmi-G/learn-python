class MyClass:
    i=12345
    def f(self):
        return 'hello world'

x=MyClass()
x.f()
xf=x.f
while True:
    print(xf())
#class may define a special method 
def __init__(self):
    self.data=[]
x=MyClass()
   
#when class defines init method,class instantiation automatically invokes init() for new-created class instnace
class Complex:
    def __init__(self,realpart,imagpart,):
        self.r=realpart
        self.i=imagpart

x=Complex(3.0,-4.5)
print(x.r,x.i)

#instance objects
x.counter=1
while x.counter<0:
    x.counter=x.counter*2
print(x.counter)
del x.counter

#method objects
x.f()  #method..(above )



