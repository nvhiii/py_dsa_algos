# Merge Two Dictionaries
# Write a function that merges two dictionaries. If a key exists in both dictionaries, add their values together; otherwise, just include the existing key-value pair. For example, given {'a': 1, 'b': 2} and {'b': 3, 'c': 4}, the output should be {'a': 1, 'b': 5, 'c': 4}.

def merge_dicts(dict1: dict, dict2: dict):
    new_dict = {}
    for key in dict1:
        new_dict[key] = dict1[key] # assigns each key to its value in new dict
    for key in dict2:
        if key in new_dict:
            if dict2[key] > new_dict[key]: # check if existing value is less
                new_dict[key] = dict2[key]
        else:
            new_dict[key] = dict2[key]

    return new_dict

