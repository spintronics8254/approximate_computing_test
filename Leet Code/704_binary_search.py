import time
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    upp = len(nums) - 1
    while True:
        if (upp - low) == 1:
            loc = -1
            break
        loc = low + int((upp - low) / 2)
        #print(low, loc, upp)
        if nums[loc] == target:
            break
        elif nums[loc] > target:
            upp = loc
        else:
            low = loc
    return loc

nums = [-1,0,3,5,9,12,14,15]
target = 3
loc = search(nums, target)
print(loc)