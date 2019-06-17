x = 1
if x == 1:
    print("x ist 1")

print("Hello, world")

mystring = "According to all known laws of levitation, bees should not be able to fly!"
print(mystring)

Combined = "Combined"
string = "String"
CombinedString = Combined + " " + string
print(CombinedString)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)


for y in mylist:
    print(y)

number = 6*7
print(number)

lotsofdamage = "Damage " *10

print(lotsofdamage)



even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

name ="johnathan"
print("hello, %s!" % name)

age = 23
print"%s is %d years old." % (name, age)

print("Your name is johnathan , and you are 23 years old.")



class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx = MyClass()

myobjectx.variable = "Boing"

print(myobjectx,variable)
print(myobjectx,variable)
