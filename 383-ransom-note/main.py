class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = defaultdict(int)

        for c in magazine:
            magazine_dict[c] += 1

        for c in ransomNote:
            if magazine_dict[c] == 0:
                return False

            magazine_dict[c] -= 1

        return True
