# ReadMe


## Install

### Python
[Python Download Site](https://www.python.org/downloads/)

get the newest version of python
Currentlly 3.70

### Text Editor or IDE

[PyCharm](https://www.jetbrains.com/pycharm/)

>other IDEs may require additional setups


## Frequently Used Code

### Comment
```
# this is a comment

'''
another way to do a comment
'''

```

### Print Text
```
print("this is text")
```

### convert to string
```
str(number)
```

### convert to integer
```
int(number)
```

### convert to float
```
float(number)
```

### get input
```
num1 = input("give me a number: ")
```

### Lists
```
friends = ["James","Jimmy","Billy"]
print(friends[0])
print(friends[1])
print(friends[2])

newFriends = ["Nic","Sue","Joe"]
friends.extend(newFriends)

print(friends[0,7])
```

### functions
```
def say_hi():
    print("Hi people!")

say_hi()
```
```
def say_hi(name):
    print("Hello " + name)

say_hi("Justin")
```
```
def average(num1,num2,num3):
    return (float(num1) + float(num2) + float(num3)) /3

avg = average(0.1,10.1,5.5)
print(avg)
```

### if-else statement
```
is_male = False

if is_male:
    print("You are male")
else:
    print("You are female")
```
```
is_male = False
is_tall = True

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are no male nor tall")
```
```
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are male and tall")
else:
    print("You are either not male or not tall or both")
```
```
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
```
def max_num(num0,num1,num2):
    if num0 >= num1 and num0 >= num2:
        return num0
    elif num1 >= num0 and num1 >= num2:
        return  num1
    else:
        return num2

    
print(max_num(1,0.1,0.2))
```

#### Compare Operators  
```
==   
>=  
<=  
!=  
```

### Dictionary   
uses key-value pair  

```
monthConversions = {
"Jan":"January",
"Feb":"Febuary",
"Mar":"March",
"Apr":"April",
"Jun":"June",
"Jul":"July",
"Aug":"August",
"Sep":"September",
"Oct":"October",
"Nov":"November",
"Dec":"December"
}

print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
```

### While Loop
```
i = 0
while i < 10:
    print(i)
    i+=1


print("done with loop")
```

### For Loop
```
for letter in "Justin Garza":
    print(letter);
```
```
friends = ["Nic","Marie","Chair","Lamp"]
for friend in friends:
    print("I love " + friend + ".")
```
```
for index in range(100):
    print(index)
```
### 2D Lists
```
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])
print(number_grid[0][1])
print(number_grid[0][2])
print(number_grid[1][0])
print(number_grid[1][1])
print(number_grid[1][2])
print(number_grid[2][0])
print(number_grid[2][1])
print(number_grid[2][2])
```

### nested for loop
```
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid:
    for col in row:
        print(row)
        print(col)
```

### Try / Except
```
try:
    value = 10/0
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError:
    print("only Chuck Norris can divide by zero")
except ValueError:
    print("that's no number")
```
>keep asking for a number until number is given
```
loop = True

while loop == True:
    try:
        number = int(input("enter a number: "))
        print(number)
        loop = False
    except:
        print("that's no number")
        loop = True
```

### Reading Files
```
## modes
# r = read
# w = write
# a = append --add only
# r+ = read and Write

## you will need to change the path 
file = open("D:\Scripts\ArchivR\ArchivR.vbs","r")

print("readable: " + str(file.readable()))

# read entire file
print(file.read())

# read each line
lineNum = 1
for line in file.readlines():
    print(str(lineNum) + " " + line)
    lineNum += 1

file.close()
```

### Writing to Files
```
## modes
# r = read
# w = write
# a = append --add only
# r+ = read and Write

# you will need to change the path 
# "r" converts to a raw string ...instead of using unicode
file = open(r"C:\Users\JGarza\Desktop\TextFile.txt","a")
file.write("new Text")

# \n is newline
file.write("new Text\n more text")

file.close()
```
```
## modes
# r = read
# w = write
# a = append --add only
# r+ = read and Write

file = open(r"C:\Users\JGarza\Desktop\TextFile.txt","w")

file.write("hello, it's bob from accounting")

file.close()
```

### Run CMD/Terminal commands
```
import os
os.system('dir c:\\')
```

### Clear Terminal
```
import os
os.system('cls')
```

### using Time
```
>>> import datetime
>>> datetime.datetime.now()
datetime(2009, 1, 6, 15, 8, 24, 78915)

>>> print(datetime.datetime.now())
2018-07-29 09:17:13.812189
```

### Modules & Pip
>modules are also refered to as packages


module file (usefulTool.py)
```
import random

feet_in_mile = 5280
metters_in_kilometer = 1000
beatles = ["John Lennon","Paul McCartney","George Harrison","Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1,num)

```

main file (app.py)
```
import usefulTools

print(usefulTools.feet_in_mile)
print(usefulTools.beatles)
```

more modules can be found at  
[Python Module Index](https://docs.python.org/3/py-modindex.html)


**internal module:**  
these are built into the python lanuage. and these are within the lib folder of your python project.

**external module:**  
these must downloaded into your python project.

#### using pip  

##### registering pip
pip is installed with python, but inorder to use it you have to register it with CMD using the following command.

```
set PATH=%PATH%;C:\...\Python\Python37-32\Scripts
```
>you'll need to change the path of course  

##### installing with pip
now you use pip with the following command
```
pip install [module name]
```
```
pip install python-docx
```

files will be stored with your python install.
```
C:\Users\JGarza\AppData\Local\Programs\Python\Python37-32\Lib\site-packages
```
##### removing modules/packages

use this to remove packages
```
pip uninstall [module name]
```

##### list all packages
use this to see all installed modules
```
pip list
```

### Classes & Objects
coming soon

### Object Functions
coming soon

### Inheritance
coming soon

### Python Interpreter
coming soon


## loop through folder/files - recursive
```
import os

movieDir ='D:\Share\Movies'

def getMovieList():
    for subdir, dirs, files in os.walk(movieDir):
        for file in files:
            print(os.path.join(subdir, file))
```



## More online Tutorials
___
### [Learn Python - Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw)

#### chapters
[(0:00) Introduction](https://www.youtube.com/watch?v=rfscVS0vtbw&t=0s)  
[(1:45) Installing Python & PyCharm](https://www.youtube.com/watch?v=rfscVS0vtbw&t=105s)  
[(6:40) Setup & Hello World](https://www.youtube.com/watch?v=rfscVS0vtbw&t=400s)  
[(10:23) Drawing a Shape](https://www.youtube.com/watch?v=rfscVS0vtbw&t=623s)  
[(15:06) Variables & Data Types](https://www.youtube.com/watch?v=rfscVS0vtbw&t=906s)  
[(27:03) Working With Strings](https://www.youtube.com/watch?v=rfscVS0vtbw&t=1623s)  
[(38:18) Working With Numbers](https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s)  
[(48:26) Getting Input From Users](https://www.youtube.com/watch?v=rfscVS0vtbw&t=2906s)  
[(52:37) Building a Basic Calculator](https://www.youtube.com/watch?v=rfscVS0vtbw&t=3157s)  
[(58:27) Mad Libs Game](https://www.youtube.com/watch?v=rfscVS0vtbw&t=3507s)  
[(1:03:10) Lists](https://www.youtube.com/watch?v=rfscVS0vtbw&t=3790s)  
[(1:10:44) List Functions](https://www.youtube.com/watch?v=rfscVS0vtbw&t=4244s)  
[(1:18:57) Tuples](https://www.youtube.com/watch?v=rfscVS0vtbw&t=4737s)  
[(1:24:15) Functions](https://www.youtube.com/watch?v=rfscVS0vtbw&t=5055s)  
[(1:34:11) Return Statement](https://www.youtube.com/watch?v=rfscVS0vtbw&t=5651s)  
[(1:40:06) If Statements](https://www.youtube.com/watch?v=rfscVS0vtbw&t=6006s)  
[(1:54:07) If Statements & Comparisons](https://www.youtube.com/watch?v=rfscVS0vtbw&t=6847s)  
[(2:00:37) Building a better Calculator](https://www.youtube.com/watch?v=rfscVS0vtbw&t=7237s)  
[(2:07:17) Dictionaries](https://www.youtube.com/watch?v=rfscVS0vtbw&t=7637s)  
[(2:14:13) While Loop](https://www.youtube.com/watch?v=rfscVS0vtbw&t=8053s)  
[(2:20:21) Building a Guessing Game](https://www.youtube.com/watch?v=rfscVS0vtbw&t=8421s)  
[(2:32:44) For Loops](https://www.youtube.com/watch?v=rfscVS0vtbw&t=9164s)  
[(2:41:20) Exponent Function](https://www.youtube.com/watch?v=rfscVS0vtbw&t=9680s)  
[(2:47:13) 2D Lists & Nested Loops](https://www.youtube.com/watch?v=rfscVS0vtbw&t=10033s)  
[(2:52:41) Building a Translator](https://www.youtube.com/watch?v=rfscVS0vtbw&t=10361s)  
[(3:00:18) Comments](https://www.youtube.com/watch?v=rfscVS0vtbw&t=10818s)  
[(3:04:17) Try / Except](https://www.youtube.com/watch?v=rfscVS0vtbw&t=11057s)  
[(3:12:41) Reading Files](https://www.youtube.com/watch?v=rfscVS0vtbw&t=11561s)  
[(3:21:26) Writing to Files](https://www.youtube.com/watch?v=rfscVS0vtbw&t=12086s)  
[(3:28:13) Modules & Pip](https://www.youtube.com/watch?v=rfscVS0vtbw&t=12493s)  
[(3:43:56) Classes & Objects](https://www.youtube.com/watch?v=rfscVS0vtbw&t=13436s)  
[(3:57:37) Building a Multiple Choice Quiz](https://www.youtube.com/watch?v=rfscVS0vtbw&t=14257s)  
[(4:08:28) Object Functions](https://www.youtube.com/watch?v=rfscVS0vtbw&t=14908s)  
[(4:12:37) Inheritance](https://www.youtube.com/watch?v=rfscVS0vtbw&t=15157s)  
[(4:20:43) Python Interpreter](https://www.youtube.com/watch?v=rfscVS0vtbw&t=15643s)  


___
### [Reading and Writing Files (IO)](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

___
### [Python Tutorial for Beginners Part 1 | Python Programming Tutorial | Python Basics](https://www.youtube.com/watch?v=2uCXIbkbDSE)