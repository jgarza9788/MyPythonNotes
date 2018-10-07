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

# is_male = False
#
# if is_male:
#     print("You are male")
# else:
#     print("You are female")
#
#
# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You are male and tall")
# elif is_male and not(is_tall):
#     print("you are male, but not tall")
# elif not(is_male) and is_tall:
#     print("you are a tall female")
# else:
#     print("You must be female")


# def max_num(num0,num1,num2):
#     if num0 >= num1 and num0 >= num2:
#         return num0
#     elif num1 >= num0 and num1 >= num2:
#         return  num1
#     else:
#         return num2

    
# print(max_num(1,0.1,0.2))


# num1 = float(input("Enter first number:"))
# op = input("Enter operator:")
# num2 = float(input("Enter second number:"))

# if op == "+":
#     print(num1+num2)
# elif op == "-":
#     print(num1-num2)
# elif op == "*":
#     print(num1*num2)
# elif op == "/":
#     print(num1/num2)
# else:
#     print("i don't know how to do that")


# monthConversions = {
# "Jan":"January",
# "Feb":"Febuary",
# "Mar":"March",
# "Apr":"April",
# "Jun":"June",
# "Jul":"July",
# "Aug":"August",
# "Sep":"September",
# "Oct":"October",
# "Nov":"November",
# "Dec":"December"
# }

# print(monthConversions["Mar"])
# print(monthConversions.get("Dec"))
# print(monthConversions.get("Luv"))


# i = 0
# while i < 10:
#     print(i)
#     i+=1

for letter in "Justin Garza":
    print(letter);


friends = ["Nic","Marie","Chair","Lamp"]
for friend in friends:
    print("I love " + friend + ".")

for index in range(100):
    print(index)