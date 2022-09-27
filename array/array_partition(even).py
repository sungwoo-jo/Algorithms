def arrayPairSum(nums: list[int]) -> int:
    sum = 0
    nums.sort() # [1, 2, 3, 4]

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum

nums = [1, 4, 3, 2]
print(arrayPairSum(nums))
