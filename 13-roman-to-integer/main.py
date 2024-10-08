class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        dict2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        res = 0
        for k, v in dict2.items():
            res += s.count(k) * v
            s = s.replace(k, "")

        for c in s:
            res += dict[c]

        return res