#1 - List to String
#Ma adjust ra ang " " na gigamit pang connect sa strings
list1 = ["Joined", "List"]
string1 = " ".join(list1)
# print(string1)


#2 - Reverse string
string2 = "Not reversed"
reversed2 = string2[::-1]
# print(reversed2)

#3 - int to String
int3 = 5678
string3 = str(int3)
# print(type(string3))

#4 - String to int
string4 = "5678"
int4 = int(string4)
# print(int4 + 5)

#5 - List comprehension
list5 = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist5 = [x for x in list5 if "a" in x]
# print(' '.join([x for x in list5 if "a" in x]))

#6 - char to ascii
char5 = 'n'
ascii5 = ord(char5)
# print(ascii5)

#7 - sep parameter sa print
# print("a", "b", sep='')

#8 - * unpack operator
def manyParams(a,b,c):
    return a+b+c
numList = [10,40,50]
# print(manyParams(*numList))
#Could also be used to print list
# print(*numList, sep=' ')

#9,10 - Ternary operator
num9 = 10
num10 = 20

# print("num9 is minimum" if num9 < num10 else "num10 is minimum")

# https://www.w3schools.com/python/ref_string_format.asp
#11 Decimal places string format
string11 = "The price will be {0:.2f}".format(49)
# print(string11)

#12 Hexadecimal string format
#Capital X for capital hexidecimal
#:b for binary
string12 = "The Hexadecimal version of {0} is {0:X}".format(255)
# print(string12)

#13,14 Percentage format
txt13 = "You scored {:%}"
# print(txt13.format(0.25))

#Or, without any decimals:

txt14 = "You scored {:.0%}"
# print(txt14.format(0.25))

#15 Format Function
# print(format(53, "08b"))

#16 Fill string with zeroes up to length for string
# print("12".zfill(5))

#17 Any() function returns if any item is true
mylist17 = [False, True, False]
# print(any(mylist17))

#18 You can multiply truth value to string
number18 = 5
# print("Even" * (number18%2==0) + "Odd" * (number18%2!=0))