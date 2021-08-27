class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            el = nums[i]
            part = target - el
            val = dic.get(part)
            if val != None:
                return [i, val]
            else:
                dic[el] = i

        return []


sol = Solution
print(str(sol.twoSum(sol, [-2,-7,11,15], -9)))
print(str(sol.twoSum(sol, [2,7,11,15], 9)))
print(str(sol.twoSum(sol, [2,7,11,15], 22)))
print(str(sol.twoSum(sol, [2,7,-11,15], 4)))
