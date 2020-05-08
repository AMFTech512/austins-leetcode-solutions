'''
Solution by Austin Fay.

This is a recursive solution for problem "2. Add Two Numbers" on leetcode.com

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# this function converts the singly-linked list into a number
def list2Num(node):
    # if we've reached our last digit, return that digit
    if node.next == None:
        return node.val

    # if we haven't reached our last digit, return the current digit plus the next digit. The next digit will be a power of 10 higher
    return node.val + list2Num(node.next) * 10

# this function converts a number into a singly-linked list
def num2List(num):
    # we want to isolate the lowest digit. We do that with the following two lines. The "nextNum" is the number without the lowest digit, and will be the number we pass down to the next call of "num2List"

    # NOTE: "//" is the integer divide operator. It will truncate the decimal after a divide operation
    # example: nextNum = 156 // 10 = 15
    nextNum = num // 10

    #example: currentDigit = 156 - (15 * 10) = 6
    currentDigit = num - (nextNum * 10)

    # if the next number is zero, we've reached our highest digit
    if nextNum == 0:
        return ListNode(num)

    # create a node with the current digit that is linked to the next digit
    return ListNode(currentDigit, num2List(nextNum))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return num2List(list2Num(l1) + list2Num(l2))


# test case; should print "156"
print(list2Num(num2List(156)))