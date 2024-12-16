from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name: str):
    search_queue = deque()
    search_queue += graph[name]
    # check if we searched person already, dont need redundancy
    searched = []
    while search_queue: # check not empty
        person = search_queue.popleft() # returns first person to check against, this delete is optimized to O(1) time
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False # if queue is empty, or person searched not found

def person_is_seller(name: str):
    return name[-1] == "m"

print(search("you"))