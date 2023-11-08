#
# @lc app=leetcode.cn id=344 lang=python3
# @lcpr version=30105
#
# [344] 反转字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1] =s[len(s)-i-1], s[i]
        
# @lc code=end



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

