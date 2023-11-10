#
# @lc app=leetcode.cn id=2300 lang=python3
# @lcpr version=30108
#
# [2300] 咒语和药水的成功对数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = [0]*len(spells)
        for i in range(len(ans)):
            target = success/spells[i]
            l = 0
            r = len(potions)-1
            while(l < r):
                mid = (l+r)//2
                if potions[mid] >= target:
                    r = mid
                else:
                    l = mid+1
            ans[i] = len(potions)-r if spells[i]*potions[r] >= success else 0
        return ans

# @lc code=end


#
# @lcpr case=start
# [5,1,3]\n[1,2,3,4,5]\n7\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n[8,5,8]\n16\n
# @lcpr case=end

#
