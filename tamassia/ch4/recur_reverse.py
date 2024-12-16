def reverse_sequence(S, start, stop):
    if start >= stop:
        return
    S[start], S[stop] = S[stop], S[start]
    reverse_sequence(S, start + 1, stop - 1)