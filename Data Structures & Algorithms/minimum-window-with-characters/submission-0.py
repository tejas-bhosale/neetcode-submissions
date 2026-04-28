class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sdict , tdict = {},{}
        if t == "" : 
            return ""
        for i in t:
            tdict[i] = 1 + tdict.get(i,0)
        have,need = 0,len(tdict)
        res,reslen = [-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c = s[r]
            sdict[c] = 1+sdict.get(c,0)

            if c in tdict and tdict[c] == sdict[c]:
                have +=1
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                sdict[s[l]]-=1
                if s[l] in tdict and sdict[s[l]] < tdict[s[l]]:
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""