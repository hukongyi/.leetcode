#
# @lc app=leetcode.cn id=350 lang=python3
# @lcpr version=30105
#
# [350] 两个数组的交集 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if(len(nums2) < len(nums1)):
            return self.intersect(nums2, nums1)
        ans = list()
        c = Counter(nums1)
        for i in nums2:
            if i in c:
                ans.append(i)
                c[i] -= 1
                if c[i] == 0:
                    c.pop(i)
        return ans
# @lc code=end


#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#
