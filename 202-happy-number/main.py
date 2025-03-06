class Solution:
    # solved this on my own
    def isHappy(self, n: int) -> bool:
        def sumSquares(n):
            sum = 0
            for i in str(n):
                sum += int(i) * int(i)
            return sum

        if n == 1:
            return True

        nums = set()
        nums.add(n)
        while True:
            n = sumSquares(n)

            if n in nums:
                return False
            else:
                nums.add(n)

            if n == 1:
                return True

        return False