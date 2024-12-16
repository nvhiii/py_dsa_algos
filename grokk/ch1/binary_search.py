# bs is better w/ tuples and flattened lists, not good w dict
# O(logn) solution, good for sorted list w/ index unknown or searching using smth other than index
phonebook = [
    ("Alice Johnson", ["123-456-7890", "234-567-8901"]),
    ("Bob Smith", ["345-678-9012"]),
    ("Carol White", ["456-789-0123", "567-890-1234"]),
    ("David Brown", ["678-901-2345"]),
    ("Emma Thompson", ["789-012-3456", "890-123-4567"]),
    ("Frank Black", ["901-234-5678"]),
    ("Grace Green", ["012-345-6789", "123-456-7890"]),
    ("Hannah Lee", ["234-567-8901"]),
    ("Ian Scott", ["345-678-9012", "456-789-0123"]),
    ("Jack Wilson", ["567-890-1234"]),
    ("Katie Young", ["678-901-2345", "789-012-3456"]),
    ("Leo King", ["890-123-4567"]),
    ("Mia Hall", ["901-234-5678", "012-345-6789"]),
    ("Nina Wright", ["123-456-7890"]),
    ("Oscar Baker", ["234-567-8901", "345-678-9012"]),
    ("Paul Reed", ["456-789-0123"]),
    ("Quinn Davis", ["567-890-1234", "678-901-2345"]),
    ("Ruby Evans", ["789-012-3456"]),
    ("Sam Collins", ["890-123-4567", "901-234-5678"]),
    ("Tina Nelson", ["012-345-6789"])
]

phonebook.sort() # ensure sorted list

def search_phonebook(pb: list, nm: str):
    lowest = 0
    highest = len(pb) - 1  

    while lowest <= highest:
        middle = (lowest + highest) // 2
        guess = pb[middle][0] # fetch name at index middle
        if guess == nm:
            return pb[middle][1]
        elif guess > nm:     # if guess is alphnum greater than name, highest is decreased
            highest = middle - 1
        else:
            lowest = middle + 1
    return None

def main():
    name = input("Please enter a name to fetch their number(s): ")
    result = search_phonebook(phonebook, name) # returns list or none
    if result is not None:
        print(f"Numbers for {name}: {result}")
    else:
        print(f"Name not found in phonebook")


if __name__ == "__main__":
    main()