n = 121   # solution to check if a number is a palindrome
num = n
result = 0
while num > 0:
    id = num %10 
    result = result * 10 + id
    num = num //10 
if n == result:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")


####
print(" to check if it is a palindrome:")

class Solution(object):
    def isPalindrome(self, num):
        result = 0
        while num > 0:
            id = num %10 
            result = result * 10 + id
            num = num //10 
        if n == result:
            return True
        else:
             return False
n = 0
ob = Solution()
print(ob.isPalindrome(n))
