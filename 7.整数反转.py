#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# 注意python负数取余的特性
# -1 % 10 = 9


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            flag = True
            x = -x
        else:
            flag = False
        while x != 0:
            if (
                res > 214748364
                or (res == 214748364 and x % 10 > 7 and not flag)
                or (res == 214748364 and x % 10 > 8 and flag)
            ):
                return 0
            res = res * 10 + x % 10
            x //= 10
        if flag:
            res = -res
        return res


# @lc code=end
