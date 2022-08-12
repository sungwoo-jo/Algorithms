# input: ["h", "e", "l", "l", "o"]
# output: ["o", "l", "l", "e", "h"]

# input: ["H", "a", "n", "n", "a", "h"]
# output: ["h", "a", "n", "n", "a", "H"]

def result(strs: list[str]) -> None:
    left, right = 0, len(strs) - 1
    while left < right:
        strs[left], strs[right] = strs[right], strs[left]
        left += 1
        right -= 1
    print(strs)

result(list(input("문자열 입력: ")))