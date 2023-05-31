#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {}
        cnt = 0
        st = 0
        en = -1
        for w in s:
            en += 1
            if mem.get(w, -1) >= 0:
                for i in range(st, mem[w]):
                    mem.pop(s[i])
                st = max(st, mem[w] + 1)
            cnt = max(cnt, en - st + 1)
            mem[w] = en
        return cnt


# @lc code=end
