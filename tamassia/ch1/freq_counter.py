from collections import deque, Counter

# def freq_counter(my_str: str, window_size: int):
#     windows = [] # store all the resulting windows here
#     # queue
#     window = deque(my_str[:window_size])
#     windows.append(dict(Counter(window)))
#     for i in range(window_size, len(my_str)):
#         removed_char = window.popleft()

#         added_char = my_str[i]
#         window.append(added_char)

#         curr_freq = windows[-1].copy() # copies prev freq dict

#         if curr_freq[removed_char] == 1:
#             del curr_freq[removed_char]
#         else:
#             curr_freq[removed_char] -= 1

#         if added_char in curr_freq:
#             curr_freq[added_char] += 1
#         else:
#             curr_freq[added_char] = 1

#         windows.append(curr_freq)

#     return windows

def freq_counter(my_str: str, window_size: int):
    windows = []
    window = deque(my_str[:window_size])
    windows.append(dict(Counter(window)))
    for i in range(window_size, len(my_str)):
        # remove last chara from last batch
        prev_trailing_chara = window.popleft()
        # add next chara
        next_chara = my_str[i] # get from iteration
        window.append(next_chara) # append next chara

        # copy last freq chart to do less work
        curr_freq = windows[-1].copy()

        if curr_freq[prev_trailing_chara] == 1: # if its only 1, its not repeated so we delete
            del curr_freq[prev_trailing_chara]
        else:
            curr_freq[prev_trailing_chara] -= 1

        if next_chara in curr_freq:
            curr_freq[next_chara] += 1
        else:
            curr_freq[next_chara] = 1

        windows.append(curr_freq)

    return windows

print(freq_counter("hello", 3))

