class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            first = heapq.heappop(neg_stones) * (-1)
            second = heapq.heappop(neg_stones) * (-1)

            diff = first - second

            if diff == 0:
                continue

            heapq.heappush(neg_stones, diff * (-1))

        if len(neg_stones) > 0:
            return neg_stones[0] * (-1)
        else:
            return 0
