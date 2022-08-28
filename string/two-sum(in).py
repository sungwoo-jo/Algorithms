# input: nums = [2, 7, 11, 15], target = 9
# output: [0, 1]

def twoSum(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums): # n = 2
        complement = target - n # complement = 9 - 2 = '7'
        if complement in nums[i + 1:]: # i + 1번째 이후 즉 현재 인덱스의 다음 인덱스부터
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)] # nums 리스트의 n(2)의 인덱스, 다음인덱스 이후에서 complement에 i+1 더한 인덱스

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))