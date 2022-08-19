# input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# output: "ball"
import collections
import re

def solution(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    # 첫번째 방법 -> defaultdict를 이용해 int 값 자동 부여하기
    # counts = collections.defaultdict(int) # 기본으로 int 값을 자동으로 부여
    # for word in words: # 위에서 가져온 단어들의 개수를 세어준다.
    #     counts[word] += 1 # 단어가 1번 등장할 때마다 1씩 증가
    # return max(counts, key=counts.get)

    # 두번째 방법 -> Counter 객체를 이용해 가장 흔하게 등장하는 단어를 most_common으로 추출
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

banned = ["hit"]
print(solution(str(input("단어를 입력: ")), banned))