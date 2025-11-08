# Python Concepts Notes (Simple Format)

## VARIABLES

* Used to store data.
* No need to declare type.
* Syntax:

```python
x = 10
name = "Shreyas"
```

## DATA TYPES

* int → whole numbers
* float → decimals
* str → text
* bool → True/False
* list → ordered collection
* tuple → fixed collection
* dict → key-value pairs
* set → unique items

## TYPE CASTING

* Convert one type to another.

```python
int("5")
float(10)
str(20)
```

## INPUT & OUTPUT

* Input always comes as string.

```python
name = input("Enter name: ")
print(name)
```

## OPERATORS

* Arithmetic: +, -, *, /, %, //, **
* Comparison: ==, !=, >, <, >=, <=
* Logical: and, or, not
* Assignment: =, +=, -=, *=, /=

## IF CONDITIONS

* Used for decision-making.

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

## LOOPS

### FOR LOOP

* Used when you know how many times to repeat.

```python
for i in range(5):
    print(i)
```

### WHILE LOOP

* Runs until condition becomes false.

```python
while condition:
    # code
```

## BREAK & CONTINUE

* break → stop loop
* continue → skip iteration

## LISTS

* Ordered, changeable.

```python
arr = [1, 2, 3]
arr.append(4)
arr.remove(2)
```

## TUPLES

* Ordered, unchangeable.

```python
t = (10, 20, 30)
```

## SETS

* Unordered, unique items.

```python
s = {1, 2, 2, 3}
```

## DICTIONARIES

* Key-value pairs.

```python
student = {"name": "Shreyas", "age": 21}
print(student["name"])
```

## FUNCTIONS

* Reusable blocks of code.

```python
def add(a, b):
    return a + b
```

## LAMBDA

* Small anonymous function.

```python
square = lambda x: x*x
```

## MODULES

* Reuse code from other files.

```python
import math
```

## FILE HANDLING

```python
f = open("data.txt", "r")
data = f.read()
f.close()
```

## EXCEPTION HANDLING

```python
try:
    x = 10/0
except ZeroDivisionError:
    print("Cannot divide")
```

## CLASSES & OBJECTS

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("BMW")
```

## INHERITANCE

```python
class A:
    pass
class B(A):
    pass
```

## OOP CONCEPTS

* Class
* Object
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism

## LIST COMPREHENSION

```python
nums = [x for x in range(5)]
```

## GENERATORS

```python
def gen():
    yield 1
    yield 2
```

## PACKAGES

```bash
pip install package_name
```
