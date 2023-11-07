#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30105
#
# [49] 字母异位词分组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            counts = [0]*26
            for ch in st:
                counts[ord(ch)-ord("a")]+=1
            mp[tuple(counts)].append(st)
        return list(mp.values())
# @lc code=end


#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#
