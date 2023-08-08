# Challenge: Finding the Missing Number


def find_missing_number(nums):
    nums.sort()  # Sort the list in-place
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
        
    return "No number missing"

# Test case
print(find_missing_number([3, 7, 1, 2, 8, 4, 6,5]))
