#!/usr/bin/env python
# coding: utf-8

# ## Body Mass Index (BMI)  
# - Input
# 1. Body Height
# 2. Body Weight

# In[1]:


name = input("What is your name? ")


# In[2]:


height = float(input("What is your height? "))


# In[3]:


weight = int(input("What is your weight? "))


# In[4]:


bmi = float(weight/height**2)
bmi


# In[5]:


print("BMI of", name, "is", bmi)


# In[7]:


if bmi == 25.0:
    print("Normal")
elif bmi < 20.0:
    print("Underweight")
elif bmi > 30.0:
    print("Overweight")
else:
    print("Be careful")


# In[ ]:




