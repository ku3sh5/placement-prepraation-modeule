# 20. Valid Parentheses

# Easy

# Companies:
# Microsoft
# Oracle
# Tekion-corp
# Flipkart
# Netflix
# Adobe
# Amazon
# Google
# Samsung
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
     def isValid(self, s):
        stack = []
        for c in list(s):
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack) <= 0 or not stack.pop() + c in ["()", "[]", "{}"]:
                    return False
        return len(stack) == 0
     
        # time complexity O(n)
        # space complexity O(n)