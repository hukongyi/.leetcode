# @lcpr-before-debug-begin
from python3problem1488 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1488 lang=python3
# @lcpr version=21917
#
# [1488] 避免洪水泛滥
#

# @lc code=start


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1]*len(rains)
        full = dict()
        pump = list()
        for i, num in enumerate(rains):
            if num == 0:
                pump.append(i)
            else:
                if num in full.keys():
                    if len(pump) <= 0:
                        return []
                    left, right = 0, len(pump)
                    target = full[num]
                    while(left < right):
                        mid = int(left + (right-left)/2)
                        if pump[mid] < target:
                            left = mid+1
                        else:
                            right = mid
                    if left == len(pump):
                        return []
                    else:
                        ans[pump.pop(left)] = num
                full[num] = i
        for i in pump:
            ans[i] = 1
        return ans


# @lc code=end

# @lcpr-div-debug-arg-start
# funName=Solution
# paramTypes= ["number[]"]
# @lcpr-div-debug-arg-end

#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0,0,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,2,0,3,0,2,0,0,0,1,2,3]\n
# @lcpr case=end

#
