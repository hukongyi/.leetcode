#
# @lc app=leetcode.cn id=275 lang=python3
# @lcpr version=30103
#
# [275] H 指数 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left=0
        right =len(citations)
        while(left<right):
            mid=left+(right-left)//2
            if(citations[mid]>=len(citations)-mid):
                right=mid
            else:
                left=mid+1
        return len(citations)-right

# @lc code=end



#
# @lcpr case=start
# [0,1,3,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,100]\n
# @lcpr case=end

#

