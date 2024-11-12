from collections import deque, Counter

def window_freq(my_str: str, window_size: int):
    windows_n_size = []
    first = deque(my_str[:window_size])
    windows_n_size.append(dict(Counter(first)))
    for i in range(window_size, len(my_str)):
        # get rid of first chara
        first_char = first.popleft()
        # add next chara
        next_chara = my_str[i]
        first.append(next_chara)

        # copy prev freq, its now current freq
        curr = windows_n_size[-1].copy()

        # first check if chara removed is in curr freq
        if curr[first_char] == 1:
            del curr[first_char]
        else:
            curr[first_char] -= 1

        # next check if next chara already in curr freq
        if next_chara in curr:
            curr[next_chara] += 1
        else:
            curr[next_chara] = 1

        windows_n_size.append(curr)

    return windows_n_size

print(window_freq("hello", 3))

