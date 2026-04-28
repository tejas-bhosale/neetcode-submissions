class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res=[]
        def backtrack(openbracket,closebracket):
            if openbracket == closebracket == n:
                res.append("".join(stack))
                return
            if openbracket < n:
                stack.append("(")
                backtrack(openbracket+1,closebracket)
                stack.pop()
            if openbracket > closebracket:
                stack.append(")")
                backtrack(openbracket,closebracket+1)
                stack.pop()

        backtrack(0,0)
        return res
        