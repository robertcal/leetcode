class Solution:
    # solved this on my own
    def longestPalindrome(self, s: str) -> int:
        dict = defaultdict(int)
        for c in s:
            dict[c] += 1

        ans = ""
        center = ""
        for key, value in dict.items():
            if value == 1:
                center = key

            while value >= 2:
                ans += key
                value -= 2

                if value == 1:
                    center = key

        ans += center + ans[::-1]

        return len(ans)

