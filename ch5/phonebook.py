def phonebook():
    pb = {}
    name = input("Enter a name to lookup: ")
    if pb.get(name): # check and return existing
        return pb[name]
    else:
        print("Name not found, creating new entry...")
        pb[name] = []
        number = input("Enter a number: ")
        pb[name].append(number)
        print("Done!")

    for person, nums in pb.items():
        print(f"{person}: {nums}")

phonebook()
