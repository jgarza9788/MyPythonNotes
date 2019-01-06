# Lesson2

## Error Handling

error handling means making sure a program doesn't fail when it runs into something unexpected.

---
### Try / Except
try a piece of code...if there is an error skip to the "except" line.  

```python
try:
    value = 10/0
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError:
    print("only Chuck Norris can divide by zero")
except ValueError:
    print("that's no number")
```

--- 

### CHALLENGE
Adjust your code from Lesson1 to not have an error.

