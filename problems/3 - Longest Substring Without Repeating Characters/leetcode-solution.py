'''
Austin Fay's Python implementation of leetcode's solution to "3. Longest Substring Without Repeating Characters"

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # i and j are the start and end indices of our current substring
        # "greatest" is the length of the longest substring with unique characters
        # "chars" is a list of characters and their last found index

        i = 0
        greatest = 0
        chars = {}

        for j in range(0, len(s)):
            # get the current character from the string
            currentChar = s[j]

            # shift the index so that the computation of the length of our substring is correct
            j += 1

            # if the current character is in our substring,
            if currentChar in chars and chars[currentChar] >= i and chars[currentChar] <= j:
                # adjust our substring so that the new start index is the one after our duplicate character
                i = chars[currentChar] + 1
            # if the current character is not in our substring, we might have encountered a bigger unique substring
            elif j - i > greatest:
                greatest = j - i
            
            #add the current character and its index to the list of characters (remember we have to shift j back)
            chars[currentChar] = j - 1

        return greatest

print(
    Solution().lengthOfLongestSubstring("abcabcbb")
)