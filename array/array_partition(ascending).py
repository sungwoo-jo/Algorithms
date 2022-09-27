def arrayPairSum(nums: list[int]) -> int:
    sum = 0
    pair = []
    nums.sort() # [1, 2, 3, 4]

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum

nums = [1, 4, 3, 2]
print(arrayPairSum(nums))
