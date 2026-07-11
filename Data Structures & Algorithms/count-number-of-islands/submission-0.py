class Solution:
    def _dfs(self, row: int, col: int, grid: List[List[str]]) -> None:
        if row >= len(grid) or col >= len(grid[0]):
            return

        if row < 0 or col < 0:
            return

        if grid[row][col] == "0":
            return

        grid[row][col] = "0"
        self._dfs(row, col + 1, grid)
        self._dfs(row + 1, col, grid)
        self._dfs(row, col - 1, grid)
        self._dfs(row - 1, col, grid)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total_islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self._dfs(row, col, grid)
                    total_islands += 1

        return total_islands
