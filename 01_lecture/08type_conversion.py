x = 10          #integer
y = 10.2        #float
z = "Hello"     #string

#implicit type conversion
x = x*y

print(type(x))

# to print class and result at the same time

print(x, type(x))
 #or
print(x, "Type of X:", type(x))

#explicit type conversion
age = input("What is your age? ")
age = int(age)
print(type(age)) #or
print(type(int(age))) #or to print answer too
print("My age is ", age, type(int(age))) 
# we can replace int with float/str

name = input("What is your name? ")
name = str(name)
print(type(name)) #or
print(type(str(name))) #or to print answer too
print("My name is ", name, type(str(name))) 