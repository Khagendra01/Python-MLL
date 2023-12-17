class MyClass:
    def __init__(self):
        z = self.checkIt(3)
        if z:
            print("cock sucker is " + str(z) )

    def checkIt(self, x):
        if x == 1:
            return 1
        elif x == 2:
            return -1
        elif x == 3:
            return 0.1

# Create an instance of MyClass
my_instance = MyClass()
