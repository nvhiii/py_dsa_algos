def sort_str_length(strings: list):
    for i in range(len(strings)):
        shortest_str_idx = i
        for j in range(i+1, len(strings)):
            if len(strings[j]) < len(strings[shortest_str_idx]):
                shortest_str_idx = j
        strings[i], strings[shortest_str_idx] = strings[shortest_str_idx], strings[i]
    return strings

my_strings = ["nahi", "wqdqwd", "wd", "wqofwegbogerr", "oiagufbwre"]
print(sort_str_length(my_strings))