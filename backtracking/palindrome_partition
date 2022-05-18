class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        part = []
        def isPalindrome(string: str):
            if not len(string):
                return False
            start = 0
            end = len(string) - 1
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(i):
            if i >= len(s):
                results.append(part[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return results
