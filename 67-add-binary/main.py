class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rev_a = a[::-1]
        rev_b = b[::-1]

        max_len = max(len(a), len(b))

        add = 0
        ans = ""
        for i in range(max_len):
            c = 0
            if i + 1 <= len(a):
                c += int(rev_a[i])

            if i + 1 <= len(b):
                c += int(rev_b[i])

            c += add
            add = 0

            if c == 3:
                ans += "1"
                add = 1
            elif c == 2:
                ans += "0"
                add = 1
            elif c == 1:
                ans += "1"
            else:
                ans += "0"

        if add == 1:
            ans += "1"

        return ans[::-1]
