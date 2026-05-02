class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            # find the delimiter '#' that ends the length prefix
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # read exactly `length` characters after the '#'
            ans.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return ans