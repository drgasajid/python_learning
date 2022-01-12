# Basic Data Structures in Python
1. Tuples
2. List
3. Dictionaries
4. Set

---

## 1. Tuples
- Ordered collection of elements
- Enclosed in () round braces / paranthesis 
- Different kinds of elements can be stored (one, two, three or all kinds)
       -- Elements: String, Float, Integer and Boolean
- Once element be stored can not be changed (unmutateable)


```python
tup1 = (1, "Python", True, 2.3)
tup1
```




    (1, 'Python', True, 2.3)



*Type of Tuple:*


```python
type(tup1)
```




    tuple



### Indexing in Tuple


```python
tup1[0]
```




    1




```python
tup1[1]
```




    'Python'




```python
tup1[2]
```




    True




```python
tup1[3]
```




    2.3



Length of indeces: tell count of elements in tuple


```python
len(tup1)
```




    4



Rnages:


```python
tup1[0:4]
```




    (1, 'Python', True, 2.3)



_last element is exclusive_

### Dealing with two tuple


```python
tup2 = (3, "Sajid", 2.5, False)
tup2
```




    (3, 'Sajid', 2.5, False)



adding two tuples (Concatinate):


```python
tup1 + tup2
```




    (1, 'Python', True, 2.3, 3, 'Sajid', 2.5, False)



Multiplying and adding (repeat + concatinate):


```python
tup1*2 + tup2
```




    (1, 'Python', True, 2.3, 1, 'Python', True, 2.3, 3, 'Sajid', 2.5, False)




```python
tup3 = (28, 26, 37, 36, 46, 57, 89)
tup3
```




    (28, 26, 37, 36, 46, 57, 89)




```python
tup3*2
```




    (28, 26, 37, 36, 46, 57, 89, 28, 26, 37, 36, 46, 57, 89)



---

## 2. List
- Ordered collection of elements
- Enclosed in [] square braces / brackets
- We can mutate them (change the values)


```python
list1 = [3, "Sajid", False]
list1
```




    [3, 'Sajid', False]




```python
type(list1)
```




    list




```python
len(list1)
```




    3




```python
list1[1]
```




    'Sajid'




```python
list1[2]
```




    False




```python
list1[0]
```




    3




```python
list2 = [430, "Python", "GitHub", 20.5, False]
list2
```




    [430, 'Python', 'GitHub', 20.5, False]



adding two or more lists (concatinate):


```python
list1 + list2
```




    [3, 'Sajid', False, 430, 'Python', 'GitHub', 20.5, False]




```python
list1*2 + list2
```




    [3, 'Sajid', False, 3, 'Sajid', False, 430, 'Python', 'GitHub', 20.5, False]



**Mutation in lists**


```python
list1.reverse()
list1
```




    [False, 'Sajid', 3]




```python
list2.remove("GitHub")
list2
```




    [430, 'Python', 20.5, False]




```python
list2.append("Animal Scientist")
list2
```




    [430, 'Python', 20.5, False, 'Animal Scientist']




```python
list2*3
```




    [430,
     'Python',
     20.5,
     False,
     'Animal Scientist',
     430,
     'Python',
     20.5,
     False,
     'Animal Scientist',
     430,
     'Python',
     20.5,
     False,
     'Animal Scientist']




```python
list3 = [(3, "Sajid", 2.5, False), (3, "Sajid", 2.5, False), (2, "Sajid", 2.5, True)]
list3
```




    [(3, 'Sajid', 2.5, False), (3, 'Sajid', 2.5, False), (2, 'Sajid', 2.5, True)]




```python
list4 = [20, 30, 60, 10, 30, 78, 90, 29, 86]
list4
```




    [20, 30, 60, 10, 30, 78, 90, 29, 86]




```python
list4.sort()
list4
```




    [10, 20, 29, 30, 30, 60, 78, 86, 90]



---

## 3. Dictionaries
- An unordered collection of elements
- Have key and value
- Enclosed in curly {} braces / brackets
- This is also mutateable/ we can change any value



```python
d1 = {"Samosa": 25, "Pakora": 80, "Chicken Roll": 35}
d1
```




    {'Samosa': 25, 'Pakora': 80, 'Chicken Roll': 35}




```python
type(d1)
```




    dict




```python
d1.keys()
```




    dict_keys(['Samosa', 'Pakora', 'Chicken Roll'])




```python
d1.values()
```




    dict_values([25, 80, 35])




```python
d1
```




    {'Samosa': 25, 'Pakora': 80, 'Chicken Roll': 35}



adding a new key and value


```python
d1["Tikki"]=10
d1
```




    {'Samosa': 25, 'Pakora': 80, 'Chicken Roll': 35, 'Tikki': 10}



update existing key or value


```python
d1["Samosa"]= 30
d1
```




    {'Samosa': 30, 'Pakora': 80, 'Chicken Roll': 35, 'Tikki': 10}



Dealing with two dictionaries:


```python
d2 = {"Choco": 200, "Candies": 80, "Lays":50}
d2
```




    {'Choco': 200, 'Candies': 80, 'Lays': 50}



Concatinate or adding two dict:


```python
d1.update(d2)
d1
```




    {'Samosa': 30,
     'Pakora': 80,
     'Chicken Roll': 35,
     'Tikki': 10,
     'Choco': 200,
     'Candies': 80,
     'Lays': 50}




```python
sum(d1.values())
```




    485



---

## 4. Set
- An unordered collection of elements
- No duplicates are allowed
- Enclosed in curly {} braces / brackets


```python
s1 = {1.1, 2, 4.2, "Sajid", 2.8, "ABG", "Biology"}
s1
```




    {1.1, 2, 2.8, 4.2, 'ABG', 'Biology', 'Sajid'}




```python
s1.add("Sajid")
s1
```




    {1.1, 2, 2.8, 4.2, 'ABG', 'Biology', 'Sajid'}




```python
s1.add(1)
s1
```




    {1, 1.1, 2, 2.8, 4.2, 'ABG', 'Biology', 'Sajid'}



---

_This file is prepared by Ghulam Asghar Sajid_
