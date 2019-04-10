# Lesson1

## Building Blocks of Programming

### Comment 
this is just a note in your program and doesn't effect how it works,  
however it can let others know what your program is doing.  

```python
# this is a comment
"""
this is another comment
"""
```
---
### Variable
this stores 1 piece of information.  
i.e. age, height, name, isAlive   

each variable has a datatype, thet describes what type of data the variable stores.  
* age = integer (whole number) (i.e. -1, 0, 1, 2, 3, 4, etc)  
* height = float (sometimes called a double) (number) (i.e. -1.5, 0.1, 1.75, etc)  
* name = string (text) (i.e. "Jason", "Serjay", etc)  
* isAlive = boolean (i.e. true or false)

```python
age = 30
name = "Justin"

print("my age is " + str(age))
print("my name is " + name)
```

> note: you can display text by using **print()**

---

### Conditional Statment (if-then Statement)
Also known as an "If-Then" statement this can let the program do something differently based on values.

```python
# Compare Operators  
"""
==   
>=  
<=  
!= 
"""

age = 15

if age < 18:
    print("not allowed to drink alcohol")
else:
    print("what would you like to drink")
```

#### more examples
```python
is_male = False

if is_male:
    print("You are male")
else:
    print("You are female")
```
```python
is_male = False
is_tall = True

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are no male nor tall")
```
```python
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are male and tall")
else:
    print("You are either not male or not tall or both")
```
```python
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("you are male, but not tall")
elif not(is_male) and is_tall:
    print("you are a tall female")
else:
    print("You must be female")
```
---
### Input from User
ask the user of the program for information.

```python
# get a name
name = input("enter your name: ")
print("your name is " + name)

# get a age
age = int(input("enter your age: "))
print("your age is " + str(age))

# get a height
height = float(input("enter your height (in feet):" ))
print("you are " + str(height) + "feet tall")

```
---
### CHALLENGE!
write a program that:
* gets info from the user
* and does an if-then statement
* and displays an output/result 

