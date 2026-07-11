class Solution:
    def _dfs(
        self,
        row: int,
        col: int,
        start_row: int,
        start_col: int,
        grid: List[List[int]],
        shape: List[Tuple],
    ) -> List[Tuple]:
        if row < 0 or col < 0:
            return shape
        if row >= len(grid) or col >= len(grid[0]):
            return shape
        if grid[row][col] == 0:
            return shape

        grid[row][col] = 0
        shape.append((row - start_row, col - start_col))
        self._dfs(row, col + 1, start_row, start_col, grid, shape)
        self._dfs(row + 1, col, start_row, start_col, grid, shape)
        self._dfs(row, col - 1, start_row, start_col, grid, shape)
        self._dfs(row - 1, col, start_row, start_col, grid, shape)

        return shape

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen_shapes = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    shape = []
                    self._dfs(row, col, row, col, grid, shape)
                    seen_shapes.add(tuple(shape))

        return len(seen_shapes)
