# return max sum possible by traveling path from top left to bottom right. only move down or right
def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]

  if r == len(grid) or c == len(grid[0]):
    return float('-inf')

  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return grid[r][c]

  down = _max_path_sum(grid, r + 1, c, memo)
  right = _max_path_sum(grid, r, c + 1, memo)

  memo[pos] = grid[r][c] + max(down, right)
  return memo[pos]
