class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        islands_size = {}
        island_id = 2  # Start island numbering at 2 because 0 and 1 are already used in the grid

        def dfs(r, c, island_id):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = island_id  # Mark this cell with the island id
            # Initialize the size with 1 (the current cell)
            size = 1
            # Recursively explore all four adjacent cells
            size += dfs(r + 1, c, island_id)  # Explore downwards
            size += dfs(r - 1, c, island_id)  # Explore upwards
            size += dfs(r, c + 1, island_id)  # Explore to the right
            size += dfs(r, c - 1, island_id)  # Explore to the left
            return size
        # Find all islands and their sizes
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    islands_size[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # If the whole grid is land or if no land, handle these edge cases
        # If there are no islands identified (i.e., no land or all land is connected)
        if not islands_size:
            # Check if there is any water in the grid
            any_water = False
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 0:
                        any_water = True
                        break
                if any_water:
                    break  
            # If there is any water cell, then converting one could create a larger island
            if any_water:
                return 1
            else:
                # If there is no water at all, the entire grid is one big island
                return m * n

        # Calculate the largest island size by converting a 0 to 1
        result = max(islands_size.values())
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    possible_size = 1
                    seen_islands = set()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 1:
                            island = grid[nr][nc]
                            if island not in seen_islands:
                                possible_size += islands_size[island]
                                seen_islands.add(island)
                    result = max(result, possible_size)

        return result