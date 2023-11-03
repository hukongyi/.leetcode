#
# @lc app=leetcode.cn id=2103 lang=python3
# @lcpr version=30102
#
# [2103] 环和杆
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        n=len(rings)//2
        print(n)
        color_count = [set() for _ in range(10)]
        for i in range(n):
            color_count[int(rings[2*i+1])].add(rings[2*i])
        ans = 0
        for i in color_count:
            if len(i)==3:
                ans+=1
        return ans
# @lc code=end



#
# @lcpr case=start
# "B0B6G0R6R0R6G9"\n
# @lcpr case=end

# @lcpr case=start
# "B0R0G0R9R0B0G0"\n
# @lcpr case=end

# @lcpr case=start
# "G4"\n
# @lcpr case=end

#

