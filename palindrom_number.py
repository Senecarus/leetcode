class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <  0:
            return False
       
        if x //10 == 0:
            return True
            
        val = str(x)
        return val == val[::-1]


sol = Solution
print("palindrom? ", sol.isPalindrome(sol, -131))

