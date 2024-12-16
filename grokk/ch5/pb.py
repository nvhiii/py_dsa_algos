class PhoneBook():
    def __init__(self):
        self.pb = {}

    # insert method
    def add_entry(self, name: str, number: str):
        if name not in self.pb: # if returns None, create
            self.pb[name] = [] # initialize new list of nums
        if number not in self.pb[name]:
            self.pb[name].append(number)

    # breadth first search for dict, later
    def search(self, name: str):
        return self.pb[name]

    # list all
    def list_all(self):
        for person, numbers in self.pb.items():
            print(f"{person}: {numbers}")

class PhoneBookApplication():
    def __init__(self):
        self.phonebook = PhoneBook() # initialize empty hashmap

    def prompts(self):
        print("Commands: ")
        print("1 - exit")
        print("2 - list all")
        print("3 - lookup name")
        print("4 - insert")

    # create list, lookup, insert here
    def list_a(self):
        self.phonebook.list_all()

    def lookup(self):
        name = input("Name: ").strip()
        nums = self.phonebook.search(name)
        if nums is None:
            print(f"{name} not found in phonebook!")
        else:
            print(f"{name}'s number(s): {nums}")

    def insert(self):
        name = input("Name: ").strip()
        number = input("Number: ").strip()
        self.phonebook.add_entry(name, number)
        print(f"Entry added: {name} - {number}")

    def execute(self):
        while True:
            self.prompts() # menu
            cmd = input("Input: ")
            if cmd == "1":
                break
            elif cmd == "2":
                self.list_a()
            elif cmd == "3":
                self.lookup()
            elif cmd == "4":
                self.insert()
            else:
                print("Invalid cmd")

app = PhoneBookApplication()
app.execute()