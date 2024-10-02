class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for str in strs:
            tmp = ""
            for i, v in enumerate(res):
                if i < len(str) and v == str[i]:
                    tmp += v
                else:
                    break

            res = tmp

        return res