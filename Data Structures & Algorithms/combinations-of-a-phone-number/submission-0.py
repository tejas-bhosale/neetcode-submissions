class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        numdict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i,chars):
            if i >= len(digits):
                res.append(chars)
                return
            for c in numdict[digits[i]]:
                dfs(i+1,chars + c)
        
        if digits:
            dfs(0,"")
        return res
        