'''
Solution by Austin Fay.

Problem "3. Longest Substring Without Repeating Characters" on leetcode.com

'''

def strWORepeats(str):
    # create a list of characters, keep track of the count of consecutively unique characters
    chars = {}
    count = 0

    # for each character in the string
    for i in str:
        # see if the current character is a duplicate
        if i in chars:
            chars[i]
            # if it is, we can stop and return the current count of consecutively unique characters
            return count
        else:
            # otherwise, add the character to our list in increase the count of consecutively unique characters
            chars[i] = 1
            count += 1
    # if we reach the end without duplicate characters, return the count
    return count

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # keep track of the length of the longest substring
        greatest = 0

        # check progressively shorter substrings to see which has the greatest substring of unique characters
        # example: "hello" -> "ello" -> "llo" -> "lo" -> "o", returns 3 because of "hel" substring
        for index in range(0, len(s)):
            substrLen = strWORepeats(s[index:])
            if substrLen > greatest:
                greatest = substrLen

        return greatest

sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))