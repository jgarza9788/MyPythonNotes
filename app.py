# Just following along with the tutorial...nothing important

# print("Yo...what up")

# print("      /|")
# print("     / |")
# print("    /  |")
# print("   /___|")


# name = "this is a name"
# number = "10000"

# print("something something")
# print("something " + number)
# print("something something")
# print("something " + name)


# print("play with numbers")
# num1 = 7.00
# num2 = 3.00
# print(num1 % num2)
# print(num1 + num2 + 0.01)


# num1 = input("give me a number: ")
# num2 = input("give me a number: ")
# num3 = input("give me a number: ")
# result = float(num1) + float(num2) + float(num3)
# print(result)

# friends = ["James","Jimmy","Billy"]
# print(friends[0])
# print(friends[1])
# print(friends[2])
#
# newFriends = ["Nic","Sue","Joe"]
# friends.extend(newFriends)
#
# friends.append("Tony")
#
# friends.insert(1,"Bruce")
#
# friends.remove("Jimmy")
#
# print(friends)
#
# print(friends.index("Tony"))
# # print(friends.index("Mike"))
#
# friends.reverse()
# print(friends)


# def say_hi():
#     print("Hi people!")
#
# say_hi()


# def say_hi(name):
#     print("Hello " + name)
#
# say_hi("Justin")

# #Start Function
# def average(num1,num2,num3):
#     return (float(num1) + float(num2) + float(num3)) /3
#
#
# #End Function
#
# avg = average(0.1,10.1,5.5)
# print(avg)

is_male = False

if is_male:
    print("You are male")
else:
    print("You are female")


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

