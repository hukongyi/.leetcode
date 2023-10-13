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
    # 定义一个避免洪水的函数，输入是一个整数列表，输出也是一个整数列表
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 初始化答案列表，长度与输入列表相同，所有元素都为-1
        ans = [-1]*len(rains)
        # 初始化一个字典，用于存储湖泊是否已满的信息
        full = dict()
        # 初始化一个列表，用于存储可以抽水的天数
        pump = list()
        # 遍历输入列表
        for i, num in enumerate(rains):
            # 如果num为0，表示这一天没有下雨，可以抽水，将这一天添加到pump列表中
            if num == 0:
                pump.append(i)
            else:
                # 如果num在full的键中，表示这个湖泊已经满了，需要抽水
                if num in full.keys():
                    # 如果pump列表为空，表示没有可以抽水的天数，返回空列表
                    if len(pump) <= 0:
                        return []
                    # 二分查找可以抽水的天数
                    left, right = 0, len(pump)
                    target = full[num]
                    while(left < right):
                        mid = int(left + (right-left)/2)
                        if pump[mid] < target:
                            left = mid+1
                        else:
                            right = mid
                    # 如果没有找到可以抽水的天数，返回空列表
                    if left == len(pump):
                        return []
                    else:
                        # 否则，将找到的这一天从pump列表中移除，并在答案列表中标记这一天抽的是哪个湖泊的水
                        ans[pump.pop(left)] = num
                # 更新湖泊的信息
                full[num] = i
        # 对于剩下的可以抽水的天数，随便抽哪个湖泊的水都可以
        for i in pump:
            ans[i] = 1
        # 返回答案列表
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
