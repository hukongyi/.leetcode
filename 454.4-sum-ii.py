#
# @lc app=leetcode.cn id=454 lang=python3
# @lcpr version=30105
#
# [454] 四数相加 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1+n2] = hashmap.get(n1+n2, 0)+1
        ans = 0
        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in hashmap:
                    ans += hashmap[-n3-n4]
        return ans
        # @lc code=end

        #
        # @lcpr case=start
        # [1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n
        # @lcpr case=end

        # @lcpr case=start
        # [0]\n[0]\n[0]\n[0]\n
        # @lcpr case=end

        #
