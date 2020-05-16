'''
Solution by Austin Fay.

Problem "4. Median of Two Sorted Arrays" on leetcode.com

'''

def mergeArrs(arr1, arr2):

    arr1len = len(arr1)
    arr2len = len(arr2)

    i1 = 0
    i2 = 0
    resultArr = []
    for i in range(0, arr1len + arr2len):
        if i1 >= arr1len:
            resultArr.extend(arr2[i2:])
            break
        elif i2 >= arr2len:
            resultArr.extend(arr1[i1:])
            break

        if arr1[i1] > arr2[i2]:
            resultArr.append(arr2[i2])
            i2 += 1
        else:
            resultArr.append(arr1[i1])
            i1 += 1
    return resultArr

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         return 0

def findMedianSortedArrays(nums1, nums2):
    mergedArr = mergeArrs(nums1, nums2)

    alen = len(mergedArr)

    if alen%2 == 0:
        return (mergedArr[alen//2] + mergedArr[alen//2 - 1])/2
    else:
        return mergedArr[alen//2]

print(findMedianSortedArrays([2, 3, 9], [1, 5, 4, 6]))