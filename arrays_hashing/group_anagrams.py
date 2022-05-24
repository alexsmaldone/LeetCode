class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
#         O(n * m log m) T | O(nm) S
#         sorted_words = {}
#         for word in strs:
#             sorted_word_list = sorted(word)
#             sorted_word = "".join(sorted_word_list)
#             if sorted_word in sorted_words:
#                 sorted_words[sorted_word].append(word)
#             else:
#                 sorted_words[sorted_word] = [word]

#         return list(sorted_words.values())

#     OPTIMAL

        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
