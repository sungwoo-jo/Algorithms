# input: "A man, a plan, a canal: Panama"
# output: true

# input: "race a car"
# output: false
import re

def solution(arr: str) -> bool:
    arr = arr.lower()
    # 정규식으로 불필요한 문자 필터링
    arr = re.sub('[^a-z0-9]', '', arr) # arr에서 a-z와 0-9가 아닌 것을 공백으로 처리하고 arr에 담아준다.

    return arr == arr[::-1] # 리스트 arr과 뒤집어진 리스트 arr을 비교한 값을 리턴

array = input("문자열 입력: ")
print(solution(array))