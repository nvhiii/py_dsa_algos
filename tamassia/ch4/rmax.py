def rmax(S, n):
    """Max of sequence S"""
    if len(S) <= 1:
        return S[0]
    else:
        rest = rmax(S, n-1)
        return max(S[n-1], rest)