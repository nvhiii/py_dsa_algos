L = [0, 1, 2, 1, 1, 0, 0, 0, 0, 1, 2, 0]
counts = [0] * 3 # only 3 numbers
for num in L:
    counts[num] += 1

print(counts)

i = 0 # pointer for the reassignment
for n in range(len(counts)):
    for _ in range(counts[n]): # print out xth index num x amt of times
        L[i] = n
        i += 1  

print(L)


# for i in range(0, len(L)):
#     for num in counts.get(num)