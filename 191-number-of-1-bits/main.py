class Solution:
    # solved this on my own
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 0:
            if n % 2:
                res += 1

            n //= 2

        return res