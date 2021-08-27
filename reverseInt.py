class Solution:
    
    def reverse(self, x: int) -> int:
        rev = 0
        MAX_VALUE,MIN_VALUE = 2**31-1,-2**31
        sign = (-1 if x < 0 else 1)
        x = abs(x)
        while x != 0:
            pop = x % 10
            x //= 10
            if (rev > MAX_VALUE/10 or (rev == MAX_VALUE / 10 and pop > 7)): return 0
            if (rev < MIN_VALUE/10 or (rev == MIN_VALUE / 10 and pop < -8)): return 0
            rev = rev * 10 + pop

        return sign * rev

print("Hello")
sol = Solution
print("result:", sol.reverse(sol, 123))
print("result:", sol.reverse(sol, 321))
print("result:", sol.reverse(sol, +321))
print("result:", sol.reverse(sol, -321))
print("result:", sol.reverse(sol, -0))
print("result:", sol.reverse(sol, +0))
print("result:", sol.reverse(sol, 0))
print("result:", sol.reverse(sol, 2147483647))
print("result:", sol.reverse(sol, -2147483647))