#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30105
#
# [383] 赎金信
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        return not ransomNote-magazine
# @lc code=end



#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end
#

