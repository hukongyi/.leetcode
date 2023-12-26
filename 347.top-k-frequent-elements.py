#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30112
#
# [347] 前 K 个高频元素
#
import heapq

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in nums:
            map_[i] = map_.get(i, 0)+1
        pri_que = []
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
# @lc code=end


#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
