class Solution:
    # solved this on my own
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key in group:
                group[key] += [s]
            else:
                group[key] = [s]

        res = []

        for k, g in group.items():
            res += [g]

        return res