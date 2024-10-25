class Solution:
    # NG
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 1

        l, r = 0, 1

        while l <= len(s) - 1:
            sublen = 1
            se = set()
            se.add(s[l])

            while r < len(s) - 1:
                if s[r] in se:
                    res = max(res, sublen)
                    break

                se.add(s[r])
                sublen += 1
                r += 1

            l += 1
            r = l + 1

        return max(res, sublen)
