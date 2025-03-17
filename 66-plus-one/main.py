class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        res = []
        add = False
        for i in range(len(digits)):
            if i == 0:
                if digits[i] + 1 == 10:
                    res.append(0)
                    add = True
                else:
                    res.append(digits[i] + 1)
            else:
                if add:
                    if digits[i] + 1 == 10:
                        res.append(0)
                        add = True
                    else:
                        res.append(digits[i] + 1)
                        add = False
                else:
                    res.append(digits[i])
                    add = False

        if add:
            res.append(1)

        res.reverse()

        return res