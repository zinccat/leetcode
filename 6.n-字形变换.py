#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        res = []
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                res.append(s[i :: 2 * numRows - 2])
            else:
                res.append(
                    self.merge(
                        s[i :: 2 * numRows - 2],
                        s[2 * numRows - 2 - i :: 2 * numRows - 2],
                    )
                )
        return "".join(res)
        # totalLen = (numRows - 1) * len(s) // (2 * numRows - 2)
        # if len(s) % (2 * numRows - 2) > 0:
        #     totalLen += 1
        # res = [["" for _ in range(totalLen)] for _ in range(numRows)]
        # for i in range(len(s)):
        #     x = i // (2 * numRows - 2)
        #     y = i % (2 * numRows - 2)
        #     if y < numRows:
        #         res[y][x * (numRows - 1)] = s[i]
        #     else:
        #         res[2 * numRows - 2 - y][x * (numRows - 1) + y - numRows + 1] = s[i]
        # return "".join(["".join(x) for x in res])

    def merge(self, s1, s2):
        res = ""
        for i in range(min(len(s1), len(s2))):
            res += s1[i] + s2[i]
        if len(s1) > len(s2):
            res += s1[len(s2) :]
        elif len(s1) < len(s2):
            res += s2[len(s1) :]
        return res


# @lc code=end
