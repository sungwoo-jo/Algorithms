# input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# output:
# [
#            ["ate","eat","tea"],
#            ["nat","tan"],
#            ["bat"]
# ]

import collections
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(list(strs)))