# input: nums = [2, 7, 11, 15], target = 9
# output: [0, 1]

def twoSum(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]] # 딕셔너리의 인덱스 조회는 해당하는 값의 인덱스를 리턴함

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))