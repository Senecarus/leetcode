class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        return list(str(int(''.join(map(str,digits))) + 1)  )

sol = Solution
print("Added one is ", sol.plusOne(sol, [9]))
print("Added one is ", sol.plusOne(sol, [1,2,3]))
print("Added one is ", sol.plusOne(sol, [9,9]))
print("Added one is ", sol.plusOne(sol, [0]))