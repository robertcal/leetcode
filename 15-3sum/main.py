class Solution:
    # solved this on my own
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        se = set()

        for k1 in list(d.keys()):
            for k2 in list(d.keys()):
                if k1 > k2:
                    continue

                if k1 == k2 and d[k1] == 1:
                    continue

                target = (k1 + k2) * (-1)

                if target == k1 and target == k2:
                    if d[target] >= 3:
                        se.add(tuple(sorted((k1, k2, target))))
                elif target == k1 or target == k2:
                    if d[target] >= 2:
                        se.add(tuple(sorted((k1, k2, target))))
                else:
                    if target in d and d[target] >= 1:
                        se.add(tuple(sorted((k1, k2, target))))

        res = []
        for s in se:
            res.append(s)

        return res
