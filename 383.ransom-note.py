#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30105
#
# [383] 赎金信
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        latterA = [0]*26
        latterB = [0]*26
        for i in list(ransomNote):
            latterA[ord(i)-ord("a")]+=1
        for i in list(magazine):
            latterB[ord(i)-ord("a")]+=1
        for i in range(26):
            if latterA[i]>latterB[i]:
                return False
        return True
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

