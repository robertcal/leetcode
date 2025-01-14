class Solution:
    # solved this on my own
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for n in nums:
            dic[n] += 1

        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

        res = []
        i = 0
        for key in dic:
            if i >= k:
                break

            res.append(key)
            i += 1

        return res