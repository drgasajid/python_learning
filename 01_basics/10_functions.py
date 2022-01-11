# when we are printing/or any fucntion many time
# like:
print("I am learning python with Dr Aammar")
print("I am learning python with Dr Aammar")
print("I am learning python with Dr Aammar")
print("I am learning python with Dr Aammar") # as much as we want

## There are many ways to define a function:
# 1: Defining a function
def print_new():
    print("I am a animal genetist + data analyst")
    print("I am a animal genetist + data analyst")
    print("I am a animal genetist + data analyst")

print_new()

# 2: Defining a function
def print_new2():
    text = "I am learning on Python"
    print(text)
    print(text)
    print(text)

print_new2()

# 3: Defining a function
def print_new3(text):
    print(text)
    print(text)
    print(text)

print_new3("I am defining a function with different ways")

# 4: Defining a function using if, else and elif
def school_calculator(age):
    if age == 5:
        print("Sajid can join the school")
    elif age > 5:
        print("Sajid should go to school immidiately")
    else:
        print("Sajid should stay at home with mom")

school_calculator(2)

# 5: Define a function of future (ML function for prediction)
def future_age(age):
    new_age = age + 20
    return new_age
future_predicted_age = future_age(18)
print(future_predicted_age)
    