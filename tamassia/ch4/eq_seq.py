from random import randint

def equality(S): # quick sort
    if len(S) <= 1:
        return S
    else:
        pidx = randint(0, len(S) - 1)
        pivot = S[pidx]
        less = [num for i, num in enumerate(S) if num <= pivot and i != pidx]
        more = [num for i, num in enumerate(S) if num > pivot and i != pidx]
        return equality(less) + [pivot] + equality(more)

