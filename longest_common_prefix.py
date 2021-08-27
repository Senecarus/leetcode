class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # strs.sort(key=len)
        # first = strs[0]

        # for i in range(len(first)):
        #     test = strs[0][:i + 1]
        #     if any( not s.startswith(test) for s in strs[1:]):
        #         return test[:-1]

        # return first
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)

sol = Solution
print("Longest prefix is ", sol.longestCommonPrefix(sol, ["reflower","flow","flight"]))
print("Longest prefix is ", sol.longestCommonPrefix(sol, ["flower","flow","flight"]))
print("Longest prefix is ", sol.longestCommonPrefix(sol, ["flo","flo","flo"]))
print("Longest prefix is ", sol.longestCommonPrefix(sol, ["aflo","bflo","dflo"]))




