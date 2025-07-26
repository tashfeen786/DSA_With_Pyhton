class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n <= 3:           
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        return True
            
n = 25
ob = Solution()
print(ob.isPrime(n))