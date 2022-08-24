# input: "babad"
# output: "bab"

# input: "cbbd"
# output: "bb"

def longestPalindrome(s: str) -> str:
	# 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]: # 확장을 하는 조건
            left -= 1
            right += 1
        return s[left + 1:right]

    if s == s[::-1] or len(s) < 2:
        return s
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key = len)
    return result

s = "babad"
print(longestPalindrome(s))