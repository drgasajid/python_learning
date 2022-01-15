#Data Visualization

## Imprting libraries
import seaborn as sns
import matplotlib.pyplot as plt

## Set a theme
sns.set_theme(style="ticks", color_codes=True)

## Import data set/own data can be imported
titanic = sns.load_dataset("titanic")
# print(titanic)

## Plot basic graph with one varibale
# plot = sns.countplot(x= "sex", data = titanic)
# plt.show()

## Plot basic graph with two varibale
plot = sns.countplot(x= "sex", data = titanic, hue = "class")
plot.set_title("Plot for basic counting from titanic data") # Adding title
plt.show()