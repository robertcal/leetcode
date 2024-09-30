class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(0, n + 1):
            count = 0
            num = i

            while num > 0:
                if num % 2:
                    count += 1

                # 2で割って、右シフトしていく
                num //= 2

            ans.append(count)

        return ans