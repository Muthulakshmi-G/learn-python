class Dog: #class name dog
    tricks=[]  #mistaken use of variable
    def __init__(self,name):
        self.name=name
    def add_trick(self,trick):
        self.tricks.append(trick)#appending to trickslist

d=Dog('fido')
e=Dog('buddy')

d.add_trick('roll over')
e.add_trick('play dead')
print (d.tricks)
