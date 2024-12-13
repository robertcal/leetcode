class Solution:
    # solved this on my own
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    q.append((r, c))

        if not fresh:
            return 0

        res = 0
        while q:
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            count = False
            for i in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr = r + dx
                    nc = c + dy
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh.remove((nr, nc))
                    count = True
            if count:
                res += 1

        if fresh:
            return -1

        return res