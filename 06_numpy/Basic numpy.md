# Array Types in Numpy

## 1-D Array


```python
import numpy as np
a = np.array([5, 5, 5])
a
```




    array([5, 5, 5])



> #### Type of array


```python
type(a)
```




    numpy.ndarray



_ndarray class is used in Numpy to represent vector and matrix_

> #### Length of array


```python
len(a)
```




    3



> #### Indexing


```python
a[0]
```




    5




```python
a[0:]
```




    array([5, 5, 5])



## 2-D Array

**List of lists**


```python
b =np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
b
```




    array([[5, 5, 5],
           [5, 5, 5],
           [5, 5, 5]])




```python
type(a)
```




    numpy.ndarray




```python
len(a)
```




    3




```python
b[0]
```




    array([5, 5, 5])




```python
b[0:]
```




    array([[5, 5, 5],
           [5, 5, 5],
           [5, 5, 5]])



## 3-D or Higher Array

For 3-D array or higher dimensional arrays, the term tensor is also commonly used

#### 2-D exis 

Exis are also called dimmensions


```python
c =np.array([[5, 5, 5], [5, 5, 5]])
c
```




    array([[5, 5, 5],
           [5, 5, 5]])



> First axis have length of 2\
> Second axis have length of 3

# How to create an array

#### 1-D


```python
d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
d
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
e = np.zeros(5)
e
```




    array([0., 0., 0., 0., 0.])




```python
f = np.empty(5)
f
```




    array([0., 0., 0., 0., 0.])




```python
g = np.ones(5)
g
```




    array([1., 1., 1., 1., 1.])



#### With range of element


```python
h = np.arange(10)
h
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])



10th is exclusive

> with specfic range


```python
i = np.arange(2, 10)
i
```




    array([2, 3, 4, 5, 6, 7, 8, 9])



> Continue with specific interval


```python
j = np.arange(2, 21, 3)
j
```




    array([ 2,  5,  8, 11, 14, 17, 20])



> Linerly spaced array


```python
j = np.linspace(2,20,num=6)
j
```




    array([ 2. ,  5.6,  9.2, 12.8, 16.4, 20. ])



> Specific data types in array


```python
k = np.ones(5, dtype=np.int8)
k
```




    array([1, 1, 1, 1, 1], dtype=int8)




```python
l = np.ones(5, dtype=np.float64)
l
```




    array([1., 1., 1., 1., 1.])



#### 2-D


```python
m = np.zeros((4, 8))
m
```




    array([[0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0.]])




```python
n = np.zeros((8, 4))
n
```




    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])




```python
o = np.empty((2, 3))
o
```




    array([[ 2. ,  5.6,  9.2],
           [12.8, 16.4, 20. ]])



#### 3-D


```python
p = np.arange(24).reshape(2, 3, 4)
p
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])


