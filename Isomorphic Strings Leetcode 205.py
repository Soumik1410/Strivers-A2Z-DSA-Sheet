class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] in mapping.keys() and mapping[s[i]] != t[i]:
                return False
            if s[i] not in mapping.keys() and t[i] in mapping.values():
                return False
            if s[i] not in mapping.keys():
                mapping[s[i]] = t[i]
            s[i] = mapping[s[i]]
        if s == t:
            return True
        else:
            return False
