def twoSum(nums, target):
    # create an empty dictionary (same as a hashtable) that will store the numbers that we've already checked
    htable = {}

    # for each number in our original array...
    for i in range(0, len(nums)):
        # compute the compliment
        compliment = target - nums[i]

        # check if the compliment is already in the dictionary (hashtable) of numbers that we've already checked. The key to speed here lies in the fact that we can easily look up the index of the compliment using the compliment itself. If the compliment is in our dictionary, it, and the number we're currently checking will add up to the target. However, if the compliment is not in our dictionary, this next line will throw an error. We use "try" to prevent that error from crashing our program
        try:
            return [i, htable[compliment]]

        # We use "except" to specify what to do in the event that the previous line threw an error (i.e. the compliment to the number that we were checking was not in our dictionary). In this case, we just want to store the number in the dictionary in hope that a future number that we check will be its compliment
        except:
            htable[nums[i]] = i

# our test case
arr = [2, 7, 11, 15]
target = 9

print(twoSum(arr, target))