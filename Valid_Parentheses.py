# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in d:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "#"
                if d[i] != top_element:
                    return False
            else:
                stack.append(i)
        return not stack


sol = Solution()
print(sol.isValid("([])"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
