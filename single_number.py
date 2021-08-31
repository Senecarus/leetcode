class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        res = 0
        for num in nums:
            res ^= num
        return res

        # dic = set()
        # for i in nums:
            
        #     # if not i in dic:
        #     #     dic.add(i)
        #     # else:
        #     #     dic.remove(i)

        #     try:
        #         dic.remove(i)
        #     except KeyError:
        #         dic.add(i)

        #     return list(dic)[0]


sol = Solution
print("Only one is: ", sol.singleNumber(sol, [4,1,2,1,2]))


