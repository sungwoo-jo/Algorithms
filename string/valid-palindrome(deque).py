import collections
from typing import Deque

# input: "A man, a plan, a canal: Panama"
# output: true

# input: "race a car"
# output: false

def solution(arr: str) -> bool:
    result = []
    # 자료형 데크로 선언
    result: Deque = collections.deque()
    for ar in arr:
        if ar.isalnum():
            result.append(ar.lower())

    while len(result) > 1:
        if result.popleft() != result.pop():
            return False
    return True


array = input("문자열 입력: ")
print(solution(array))