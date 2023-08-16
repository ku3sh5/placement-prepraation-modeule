# 1143. Longest Common Subsequence
# Medium

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)     
        sub1, sub2 = [0]*(n2+1), [0]*(n2+1)  
        for i in range(n1):                
            for j in range(n2):            
                if text1[i] == text2[j]:  
                    sub2[j+1] = 1 + sub1[j]  
                elif sub2[j] > sub1[j+1]:   
                    sub2[j+1] = sub2[j]       
                else:                      
                    sub2[j+1] = sub1[j+1]    
            sub2, sub1 = sub1, sub2            
        return sub1[-1]                     
    
# Time Complexity: O(m*n)
# Space Complexity: O(n)