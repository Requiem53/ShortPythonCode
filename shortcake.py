from typing import List
#Given string, all sorted lowercase letters are ahead of uppercase
#All sorted uppercase are ahead of digits
#All sorted odd digits are ahead of even digits
def ginortS(s: str) -> str:
    lowercase = []
    uppercase = []
    odd = []
    even = []
    
    for char in s:
        if char.isalpha():
            if char.islower():
                lowercase.append(char)
            else:
                uppercase.append(char)
        else:
            if int(char) % 2 == 0:
                even.append(char)
            else:
                odd.append(char)
                
    lowercase.sort()
    uppercase.sort()
    odd.sort()
    even.sort()
    
    stringList = [lowercase, uppercase, odd, even]
        
    return ''.join([''.join(string) for string in stringList])

# wtf na answer sa babaw
# S = input()

# def s(x):
#     if x.islower():
#         return ord(x)
#     elif x.isupper():
#         return ord(x)*100000
#     elif x in "13579":
#         return ord(x)*10000000000
#     else:
#         return ord(x)*1000000000000000000

# print(*sorted(S, key=s), sep='')

#Capitalize first letter
def capitalizeFirst(s : str) -> str:
    spaced = s.split(' ')
    full = []
    for name in spaced:
        full.append(name.capitalize())
    return ' '.join(full)

#Valid Parentheses
def isValid(s: str) -> bool:
    ack = []
    lookfor = {')':'(', '}':'{', ']':'['}

    for p in s:
        if p in lookfor.values():
            ack.append(p)
        elif ack and lookfor[p] == ack[-1]:
            ack.pop()
        else:
            return False

    return ack == []

#Longest common prefix
def longestCommonPrefix(strs: List[str]) -> str:
    ans = ""
    for i in range(len(min(strs))):
        s = strs[0][i]
        for j in range(len(strs)):
            if strs[j][i] != s:
                return ans
        
        ans += s
    
    return ans

#Roman to Int
def romanToInt(s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    number = 0
    for char in s:
        number += translations[char]
    return number

#Palindrome
def isPalindrome(x: int) -> bool:
    a = str(x)
    return a == a[::-1] 

#Two sum
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

#Fibonacci get term in x
fib = lambda x: x if x <2 else fib(x-1) + fib(x-2)


