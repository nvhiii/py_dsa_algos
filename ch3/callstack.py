def greet(name: str):
    print(f"Hello, {name}!")
    greet_special(name)
    print("Prepping to say bye...")
    bye()

def greet_special(name: str):
    print(f"Hey pookie {name}")

def bye():
    print("Bye!")

greet("nahi")