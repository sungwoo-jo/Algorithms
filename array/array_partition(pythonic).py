def arrayPairSum(nums: list[int]) -> int:
    return sum(sorted(nums)[::2]) # 배열의 짝수번째를 더하여 리턴

nums = [1, 4, 3, 2]
print(arrayPairSum(nums))
