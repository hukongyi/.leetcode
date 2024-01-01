#
# @lc app=leetcode.cn id=1599 lang=python3
# @lcpr version=30112
#
# [1599] 经营摩天轮的最大利润
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if len(customers) == 0:
            return -1
        maxpay = 0
        pay = 0
        maxi = -2
        waitcustomers = 0
        for i, customer in enumerate(customers):
            waitcustomers += customer
            if waitcustomers >= 4:
                waitcustomers -= 4
                pay += 4*boardingCost
            else:
                pay += waitcustomers*boardingCost
                waitcustomers = 0
            pay -= runningCost
            if pay > maxpay:
                maxpay = pay
                maxi = i
        while waitcustomers > 0:
            i += 1
            if waitcustomers >= 4:
                waitcustomers -= 4
                pay += 4*boardingCost
            else:
                pay += waitcustomers*boardingCost
                waitcustomers = 0
            pay -= runningCost
            if pay > maxpay:
                maxpay = pay
                maxi = i
        return maxi+1

        # @lc code=end

        #
        # @lcpr case=start
        # [8,3]\n5\n6\n
        # @lcpr case=end

        # @lcpr case=start
        # [10,9,6]\n6\n4\n
        # @lcpr case=end

        # @lcpr case=start
        # [3,4,0,5,1]\n1\n92\n
        # @lcpr case=end

        #
