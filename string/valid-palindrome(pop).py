# input: "A man, a plan, a canal: Panama"
# output: true

# input: "race a car"
# output: false

def solution(arr: str) -> bool:
    result = []
    for ar in arr:
        if ar.isalnum():
            result.append(ar.lower())

    print(result)

    # 팰린드롬 여부 판별
    while len(result) > 1:
        if result.pop(0) != result.pop():
            return False
    return True

array = input("문자열 입력: ")
print(solution(array))