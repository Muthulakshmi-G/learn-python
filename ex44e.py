class Other(object):

    def override(self):
        print("other override()")

    def implicit(self):
        print("other impliocit")
    def altered(self):
        print("other altered()")

class Child(object):
    def __init__(self):
        self.other=Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("child override")

son=Child()

son.implicit()
son.override()
