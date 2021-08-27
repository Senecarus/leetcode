class Solution:
    def isValid(self, s: str) -> bool:
        
        if (len(s) % 2 != 0):
            return False
        opened = "{(["
        closed = "})]"
        relDic = {'}': '{', ')': '(',']': '['}
        stack= []

        for i in range(len(s)):
            ch = s[i]
            if ch in opened:
                stack.append(ch)
            else:
                if ch in closed:
                    if len(stack) == 0 or relDic.get(ch) != stack[-1]:
                        return False
                    stack.pop()

        return len(stack) == 0

sol = Solution

print("Parentheses are vaid ", sol.isValid(sol, "({{{{}}}))"))
print("Parentheses are vaid ", sol.isValid(sol, "{}"))
print("Parentheses are vaid ", sol.isValid(sol, "()"))
print("Parentheses are vaid ", sol.isValid(sol, "){"))
print("Parentheses are vaid ", sol.isValid(sol, "["))
print("Parentheses are vaid ", sol.isValid(sol, "(("))
print("Parentheses are vaid ", sol.isValid(sol, "({()})"))
print("Parentheses are vaid ", sol.isValid(sol, "({(})})"))




