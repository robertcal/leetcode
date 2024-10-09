class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]

        if target == color:
            return image

        q = deque([(sr, sc)])
        row, col = len(image), len(image[0])

        image[sr][sc] = color

        while q:
            x, y = q.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < row and 0 <= my < col and image[mx][my] == target:
                    q.append((mx, my))
                    image[mx][my] = color

        return image
