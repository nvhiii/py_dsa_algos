# assume arr exists
def heapify(arr): # turn into heap
    # first make it into a complete binary tree
    # ensure good indexing as well
    arr.append(arr[0]) # we basically ignore 0th index
    curr = (len(arr) - 1) // 2 # first non leaf "node", aka index
    while curr > 0:
        i = curr

        while 2 * i < len(arr):
            left = 2 * i
            right = 2 * i + 1
            lower = left

            # check if lower is actually left
            if right < len(arr) and arr[right] < arr[left]:
                lower = right

            if arr[i] > arr[lower]:
                arr[i], arr[lower] = arr[lower], arr[i]
                i = lower
            else:
                break

        curr -= 1