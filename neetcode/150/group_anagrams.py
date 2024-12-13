from collections import defaultdict

def group_anagrams(strs: list) -> list:
    my_dict = defaultdict(list)
    for s in strs:
        count = [0] * 26 # ascii mapping
        for c in s:
            count[ord(c) - ord("a")] += 1
        my_dict[tuple(count)].append(s)
    return my_dict.values()

my_strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams(my_strs))