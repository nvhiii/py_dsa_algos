# O(n^2) time solution, two operations done on data
def find_smallest(arr: list):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(arr: list):
    new = []
    for i in range(len(arr)):
        smallest_idx = find_smallest(arr) # get smallest idx
        new.append(arr.pop(smallest_idx)) # removes smallest from array, and adds to new, (pop returns removed item)
    return new

def main():
    my_list = [5, 3, 6, 2, 10]
    print(selection_sort(my_list))

if __name__ == "__main__":
    main()