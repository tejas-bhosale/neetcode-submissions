class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for ch in s:
            if ch not in sdict.keys():
                sdict[ch] =0 
            sdict[ch]+=1
        
        for ch in t:
            if ch not in tdict.keys():
                tdict[ch] =0 
            tdict[ch]+=1
        
        for ch in s:
            if sdict.get(ch) != tdict.get(ch):
                return False
        
        for ch in t:
            if sdict.get(ch) != tdict.get(ch):
                return False
        return True

        


        