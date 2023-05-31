#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash即可
        hash_map = {}
        for idx, num in enumerate(nums):
            if hash_map.get(target - num, -1) >= 0:
                return [hash_map[target - num], idx]
            hash_map[num] = idx


# @lc code=end
