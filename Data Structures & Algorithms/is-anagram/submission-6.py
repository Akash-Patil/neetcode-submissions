class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method
        # Put both in a map and compare the maps to see if equal

        mp1 = {}
        mp2 = {}

        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            mp1[s[i]] = mp1.get(s[i], 0) + 1

        for j in range(len(t)):
            mp2[t[j]] = mp2.get(t[j], 0) + 1

        return (mp1 == mp2)

