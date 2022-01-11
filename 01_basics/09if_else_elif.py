req_age_for_school = 5
sajid_age = 4

# question: can Sajid go to school?

if sajid_age == req_age_for_school:
    print("Sajid can go to school")
else:
    print("Sajid can not go to school") 
# or should go to higher classes if age is not equal but greater than required age
# if age is greater than requir age than:

if sajid_age == req_age_for_school:
    print("Sajid can go to school")
elif sajid_age > req_age_for_school:
    print("Sajid should be in higher classes")
elif sajid_age < 2:
    print("Sajid should stay at home") # we can add many conditions
else:
    print("Sajid can not go to school") 