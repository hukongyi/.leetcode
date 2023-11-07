#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=30105
#
# [242] 有效的字母异位词
#

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a==b
# @lc code=end



#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#

