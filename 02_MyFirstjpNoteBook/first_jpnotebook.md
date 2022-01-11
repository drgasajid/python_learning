# Python Learning
## working on Jupytor Notebook
### Basics
1. My first notebook
2. I am making markdown file


```python
print(2+3+4+5)
print("My name is Dr Ghulam Asghar Sajid")
print("I want to be a data analyst")
```

**Jupytor don't show comments (with #) in a coding cell e.g; # String Varibale


```python
y = "My name is Ghulam Asghar Sajid"  # String Variable
y
```

### Operators


```python
print(2+1)
print(673-623)
print(6728/23)
print(673*72)
print(6729%13)
print(6728//23)
print(781**3)
print(673**3/78-34+7823/23*2)
```

### Strings


```python
print("My name is Dr Ghulam Asghar Sajid")
print("I want to be a data analyst")
print('test for single col')
print("test for double col")
print('''test for triple col''')
```

**Quotation marks; inverted comma (single or double or triple) are same in Python

### Varibales

Variables: Object containing specific values


```python
x = 5  # Numeric or Integer Variable
print(x)

y = "My name is Ghulam Asghar Sajid"  # String Variable
print(y)
```

**Update if you re-suppose


```python
x = 25
print(x)

x = x-7 # Or you can update your previsou suppose value in any way
print(x)
```

**Type/Class of variables**


```python
type(x)
print(type(x))
print(type(y))
```

Rules to assign a variable/object:
1. The variable should contain letters, numbers or underscores
2. Do not start with numbers
3. Spaces are not allowed
4. Do not use keywords already used in python functions (break, mean, medium, test etc)
     _You can search function in python using Google_
5. Variable name should be short and descriptive
6. Case sensitivety (Try to use lower case variable)


```python
fruit_basket = "Apple, Apple, Orange"  
print(fruit_basket)
print(type(fruit_basket))

fruit_basket = 3
print(fruit_basket)
print(type(fruit_basket))
```

To delete:


```python
del fruit_basket
```

**Desireable Variables**


```python
fruit_basket="Mangoes"
print(fruit_basket)
```

To create function on desire

_input function_



```python
fruit_basket=input("which is your favorite fruit? ")
print(fruit_basket)
```

## Conditional Logics
| Name | Sign |
| :--- | :---: |
|equal to | == |
|not equal to | != |
|less than | < |
|greator than | > |
|less than & equal to | <= |
|greator than & equal to | >= |

_Logical operators are eithers "true or false" or "yes or no" or "0 or 1"_


