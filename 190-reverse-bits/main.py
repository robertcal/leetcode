class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:].zfill(32)

        reverseBits = int(bits[::-1], 2)

        return reverseBits