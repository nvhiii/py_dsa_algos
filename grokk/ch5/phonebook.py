pb = {}

def phonebook(my_dict: dict):
    name = input("Enter a name to lookup: ")
    if my_dict.get(name): # check and return existing
        return my_dict[name]
    else:
        print("Name not found, creating new entry...")
        my_dict[name] = []
        number = input("Enter a number: ")
        my_dict[name].append(number)
        print("Done!")

    for person, nums in my_dict.items():
        print(f"{person}: {nums}")

# phonebook(pb)
print(pb)