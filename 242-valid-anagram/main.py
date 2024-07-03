class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c not in hash:
                hash[c] = 1
            else:
                hash[c] += 1

        for c in t:
            if c not in hash:
                return False

            hash[c] -= 1

        ans = True
        for i, v in hash.items():
            if v != 0:
                ans = False

        return ans