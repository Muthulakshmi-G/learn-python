class Car():
    airbag_used=False
    def met_acc(self):
        self.airbag_used=True
"""In general, any operation performed using self will always make that operation specific to the instance/object who called the function and the result of which will be not be dedicated to other objects until they themselves call the same function again."""
ferrari=Car()
ferrari.met_acc()
a=ferrari.airbag_used

jaguar=Car()
print(jaguar.airbag_used)

benz=Car()
print(benz.airbag_used)


print(a)

print('Ferrari airbag memory location is: {}'.format(id(ferrari.airbag_used)))
print(' Jaguar airbag memory location is: {}'.format(id(benz.airbag_used)))
"""print('   Benz airbag memory location is: {}'.format(id(Jaguar.airbag_used)))"""
