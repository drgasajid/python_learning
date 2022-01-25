# Working on Chilla data

### Importing library
```
import pandas as pd
```
### Importing data from local directory
```
chilla = pd.read_csv("data_viz.csv")
print(chilla)
```
### Importing libraries for plotting
```
import seaborn as sns
import matplotlib.pyplot as plt
```
### Setting theme
```
sns.set_theme(style = "ticks", color_codes = True)
```
### Plotting graph for gender
```
plot = sns.countplot(x = "gender", hue = "age", data = chilla)
plt.show()
```
### Plotting for availibilty of time
```
plot = sns.countplot(x = "gender", hue = "time_of_class(time)", data = chilla)
plt.show()
```
### Plotting a pair plot
```
plot = sns.pairplot(data= chilla, hue="gender")
plt.show()
```
