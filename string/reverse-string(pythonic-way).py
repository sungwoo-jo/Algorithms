# input: ["h", "e", "l", "l", "o"]
# output: ["o", "l", "l", "e", "h"]

# input: ["H", "a", "n", "n", "a", "h"]
# output: ["h", "a", "n", "n", "a", "H"]

def result(strs: list[str]) -> None:
    s = []
    # strs = list(reversed(strs)) # reversed() 함수를 사용
    # strs.reverse()  # reverse() 함수를 사용
    s[:] = strs[::-1] # 문자열 슬라이싱 사용
    print(s)

result(list(input("문자열 입력: ")))