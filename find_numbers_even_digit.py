# Input: nums = [12,345,2,6,7896]
# Output: 2

nums = [5556,9010,482,12]

def find_count(nums):
    count = 0
    for ele in range(len(nums)):
        if len(str(nums[ele])) % 2 == 0:
            count+=1
    return count

result = find_count(nums)
print(result)
