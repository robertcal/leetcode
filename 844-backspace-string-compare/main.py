class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        self.s1 = []
        self.s2 = []

        for c in s:
            if c == "#":
                if len(self.s1):
                    self.s1.pop()
            else:
                self.s1.append(c)

        for c in t:
            if c == "#":
                if len(self.s2):
                    self.s2.pop()
            else:
                self.s2.append(c)

        return self.s1 == self.s2