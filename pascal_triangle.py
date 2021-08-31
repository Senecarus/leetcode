class Solution:
        # def generate(self, numRows: int) -> list[list[int]]:


        # pascal = [[1]*(i+1) for i in range(numRows)]
        # for i in range(numRows):
        #     for j in range(1,i):
        #         pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        # return pascal

        # res = [[1]]
        # for _ in range(1, numRows):
        #     res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        # return res[:numRows]


        def recursive (self, numRows: int, l: list[list[int]])-> list[list[int]]:
            
            if len(l) == numRows:
                return l


            tmp = []
            for i in range(len(l) - 1):
                tmp.append (l[-1][i + 1] + l[-1][i])

            
            return Solution.recursive(self, numRows, l + [[1] + tmp + [1]])

        def generate(self, numRows: int) -> list[list[int]]:
            if numRows == 0:
                return []

            return Solution.recursive(self, numRows, [[1]])
        
    

sol = Solution
print("Pascal's triangle", sol.generate(sol, 6))
print("Pascal's triangle", sol.generate(sol, 5))
print("Pascal's triangle", sol.generate(sol, 4))
print("Pascal's triangle", sol.generate(sol, 3))
print("Pascal's triangle", sol.generate(sol, 1))
print("Pascal's triangle", sol.generate(sol, 2))