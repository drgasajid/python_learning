# There are 'while' and 'for' loops

# While Loops

x = 0
while (x < 5):
    print(x)
    x = x + 1


# For Loops

for x in range (5, 10):
    print(x)

# Uning this loop in a program
# when we make an array (assume data)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days: # d assigned as loop for days
    print(d)  # for continous loop

for d in days:
    if (d == "Fri"): break
    print(d)    # To break/stop the loop at specific point (Fri)

for d in days:
    if (d == "Fri"): continue
    print(d)    # To skip the loop at specific point (Fri)

## There are many other for loops in advance level

