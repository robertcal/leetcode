class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        deq = collections.deque()

        for t in tokens:
            if t == "+":
                b = deq.pop()
                a = deq.pop()
                deq.append(a + b)
            elif t == "-":
                b = deq.pop()
                a = deq.pop()
                deq.append(a - b)
            elif t == "*":
                b = deq.pop()
                a = deq.pop()
                deq.append(a * b)
            elif t == "/":
                b = deq.pop()
                a = deq.pop()
                deq.append(int(a / b))
            else:
                deq.append(int(t))

        return deq.pop()