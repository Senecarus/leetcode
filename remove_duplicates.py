class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s = set(nums)
        nums = list(s)
        nums.sort()
        print(nums)
        return len(nums)
        

sol = Solution
l = [1,1,2]
print("Duplicates removed ", sol.removeDuplicates(sol, l), l)





