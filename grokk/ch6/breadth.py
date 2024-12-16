from collections import deque

friends = {}
friends["me"] = [("nafiz", "homeless"), ("mim", "swe"), ("marvin", "banker"), ("moose", "ceo"), ("tush", "student"), ("reesh", "payroll")]
friends["nafiz"] = []
friends["mim"] = []
friends["marvin"] = []
friends["moose"] = []
friends["tush"] = []
friends["reesh"] = []

def my_bfs(first_person: str):
    queue = deque()
    queue += friends[first_person]
    searched = []
    while queue:
        person = queue.popleft() # returns the list of tuples of friends
        if person[0] not in searched:
            if find_hobo(person):
                print(f"{person} is homeless!")
                return True
            else:
                queue += friends[person]
                searched.append(person)

    return False


def find_hobo(person):
    return person[1] == "homeless"
