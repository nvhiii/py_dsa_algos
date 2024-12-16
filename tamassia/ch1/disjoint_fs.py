# Check for Disjoint Frozensets
# Write a function that takes two frozensets and returns True if they are disjoint (have no elements in common), otherwise False. For example, given frozenset([1, 2, 3]) and frozenset([4, 5]), the output should be True.

def disjoint_fs(fs: frozenset, fs2: frozenset):
    return len(fs & fs2) == 0