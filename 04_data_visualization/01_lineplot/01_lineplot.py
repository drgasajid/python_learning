#!/usr/bin/env python
# coding: utf-8

# # Line Plot
# ### Importing libraries

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# ### Loading data set from built-in seaborn datasets

# In[2]:


flower = sns.load_dataset("iris")
flower


# ### Drawing a line plot

# In[3]:


sns.lineplot(x = "sepal_length", y = "sepal_width", data = flower)
plt.show()


# ### Adding title

# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt

flower = sns.load_dataset("iris")

sns.lineplot(x = "sepal_length", y = "sepal_width", data = flower)
plt.title("Plot for Sepal length and width of flowers") #adding title
plt.show()


# ### Adding limits

# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt

flower = sns.load_dataset("iris")

sns.lineplot(x = "sepal_length", y = "sepal_width", data = flower)
plt.title("Plot for Sepal length and width of flowers")
plt.xlim(2) # adjusting x limit
plt.ylim(1) # adjusting y limit
plt.show()


# ### Setting Style with matplotlib

# In[6]:


from matplotlib import style

print(plt.style.available)


# In[8]:


sns.lineplot(x = "sepal_length", y = "sepal_width", data = flower)
plt.title("Plot for Sepal length and width of flowers")
plt.style.use("dark_background")
plt.show()


# ### Setting style with seaborn
# The set_style() function is used to set the theme for the plot. It can accept the following values - dark, white, whitegrid, darkgrid and tickers. The dark and darkgrid parameters provide a grey background without and with grids, respectively. Similarly, we can conclude for the white and whitegrid parameters.

# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt

flower = sns.load_dataset("iris")

sns.lineplot(x = "sepal_length", y = "sepal_width", data = flower)
sns.set_style("dark")
plt.title("Plot for Sepal length and width of flowers")
plt.show()


# ### Figure Size

# In[31]:


import seaborn as sns
import matplotlib.pyplot as plt

flower = sns.load_dataset("iris")

plt.figure(figsize=(12,6))

sns.lineplot(x = "petal_length", y = "petal_width", data = flower)
plt.title("Plot for Petal length and width of flowers")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.style.use("Solarize_Light2")

plt.show()


# In[ ]:




