class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        initNum = image[sr][sc]
        if image[sr][sc] == color:
            return image

        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = []
        queue.append((sr, sc))

        seen = []
        while queue:
            item = queue.pop(0)
            x, y = item[0], item[1]
            seen = []
            seen.append((x, y))

            if image[x][y] == initNum:
                image[x][y] = color
            else:
                continue

            for d in direction:
                dx, dy = d[0], d[1]
                if not (x + dx, y + dy) in seen and (x + dx >= 0 and x + dx < m) and (y + dy >= 0 and y + dy < n):
                    queue.append((x + dx, y + dy))

        return image