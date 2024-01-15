#
# @lc app=leetcode.cn id=2085 lang=python3
# @lcpr version=30112
#
# [2085] 统计出现过一次的公共字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_counter = Counter(words1)
        words2_counter = Counter(words2)
        ans = sum(
            [
                1
                for i in words1_counter
                if words1_counter[i] == 1 and words2_counter.get(i, 0) == 1
            ]
        )
        return ans


# @lc code=end


#
# @lcpr case=start
# ["leetcode","is","amazing","as","is"]\n["amazing","leetcode","is"]\n
# @lcpr case=end

# @lcpr case=start
# ["b","bb","bbb"]\n["a","aa","aaa"]\n
# @lcpr case=end

# @lcpr case=start
# ["a","ab"]\n["a","a","a","ab"]\n
# @lcpr case=end

#
