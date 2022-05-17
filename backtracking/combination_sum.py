class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def dfs(i, current, total):
            print(current, total)
            if total == target:
                combinations.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return combinations
