#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 使用栈, 注意顺序
        d = {"(": ")", "{": "}", "[": "]"}
        st = []
        for c in s:
            if c in d:
                st.append(c)
            elif not st or d[st.pop()] != c:
                return False
        return not st
        # cnt = [0, 0, 0]
        # for c in s:
        #     if c == "(":
        #         cnt[0] += 1
        #     elif c == ")":
        #         if cnt[0] == 0:
        #             return False
        #         cnt[0] -= 1
        #     elif c == "[":
        #         cnt[1] += 1
        #     elif c == "]":
        #         if cnt[1] == 0:
        #             return False
        #         cnt[1] -= 1
        #     elif c == "{":
        #         cnt[2] += 1
        #     elif c == "}":
        #         if cnt[2] == 0:
        #             return False
        #         cnt[2] -= 1
        #     else:
        #         return False

        # return cnt[0] == cnt[1] == cnt[2] == 0


# @lc code=end
