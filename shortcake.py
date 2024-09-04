from typing import List
#One liner Fizz Buzz
#Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if both
print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1,101)))


# You are given two positive integers n and k.
# You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
# Return the number of changes needed to make n equal to k. If it is impossible, return -1.

def minChanges(n: int, k: int) -> int:
    if n == k:
        return 0
    n_binary = format(n, "b").zfill(32)
    k_binary = format(k, "b").zfill(32)
    if any(k_binary[i] == "1" and n_binary[i] == "0" for i in range(len(n_binary))):
        return -1
    return sum(k_binary[i] == "0" and n_binary[i] == "1" for i in range(len(n_binary)))
# print(minChanges(13,4))
        

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
# print(ginortS("Sorting1234"))


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
# print(capitalizeFirst("hello world"))


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
# print(isValid("({[}])"))


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
# print(longestCommonPrefix(["flower", "flow", "flight"]))


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
# print(romanToInt("CMXVII"))


#Palindrome
def isPalindrome(x: int) -> bool:
    a = str(x)
    return a == a[::-1] 
# print(isPalindrome(505))


#Two sum
#Two numbers from list add up to target then return indices
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
# print(twoSum([2,11,7,5], 9))


#Fibonacci get term in x
fib = lambda x: x if x <2 else fib(x-1) + fib(x-2)
# print(fib(5))


