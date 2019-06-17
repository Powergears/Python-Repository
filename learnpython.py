

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "Boing"

print(myobjectx.variable)
print(myobjecty.variable)


count = 0
while count < 5:
    print(count)
    count += 1
