# Indexing

Sample String


```python
mystr = "My Pen"
mystr
```




    'My Pen'



_*to check the length of indeces_


```python
len(mystr)
```




    6



Index start from 0 so that if length of indeces = 6, last index will be 5, as follows:


```python
mystr[0]
```




    'M'




```python
mystr[1]
```




    'y'




```python
mystr[2]
```




    ' '



_*space is also a index_


```python
mystr[3]
```




    'P'




```python
mystr[4]
```




    'e'




```python
mystr[5]
```




    'n'



Printing range of indeces


```python
mystr[0:3]
```




    'My '




```python
mystr[0:6]
```




    'My Pen'



_last index will be exclusive_ as length is 6 and index is starting from zero, total alphbets are 6 including 1 space.


```python
mystr[-1]
```




    'n'




```python
mystr[-2]
```




    'e'




```python
mystr[-3]
```




    'P'



if we put - index number, it starts indexing from end of the string


```python
mystr[-3:-1]
```




    'Pe'




```python
mystr[-3:6]
```




    'Pen'




```python
mystr[-4:6]
```




    ' Pen'



It is not removing first 4 indeces but printing last 4 out of total string length (6).

## String Methods


```python
food = "pizza is very hot"
food
```




    'pizza is very hot'




```python
len(food)
```




    17



First letter capitalize


```python
food.capitalize()
```




    'Pizza is very hot'



All letters upper case


```python
food.upper()
```




    'PIZZA IS VERY HOT'



All letters lower case


```python
food.lower()
```




    'pizza is very hot'



To replace any thing in string:


```python
food.replace("very", "not")
```




    'pizza is not hot'



To count a specific alphabets in a string (Used in Sequencing Reads)


```python
seq = "AGTCAAGTCCAATCCCTAGGCATCC"
seq
```




    'AGTCAAGTCCAATCCCTAGGCATCC'




```python
seq.count("A")
```




    7




```python
seq.count("ATC")
```




    2



### Finding an index number in a string


```python
seq = "AGTCAAGTCCAATCCCTAGGCATCC"
seq
```




    'AGTCAAGTCCAATCCCTAGGCATCC'




```python
seq.find("ATC")
```




    11




```python
name = "My name is Ghulam Asghar Sajid"
name
```




    'My name is Ghulam Asghar Sajid'




```python
name.find("S")
```




    25




```python
name.find("s")
```




    9



_so it is case sensitive_

### Spliting a string


```python
animals = "I have dog, cat, cattle, alephent, lion and sheep"
animals
```




    'I have dog, cat, cattle, alephent, lion and sheep'




```python
animals.split(",")
```




    ['I have dog', ' cat', ' cattle', ' alephent', ' lion and sheep']



_splitted on the bases of ,_
