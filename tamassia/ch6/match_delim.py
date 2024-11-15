from arraystack import ArrayStack

def matched(expr):
    lefts = "{(["
    rights = "})]"
    stack = ArrayStack()
    for bracket in expr:
        if bracket in lefts:
            stack.push(bracket)
        elif bracket in rights:
            if stack.is_empty(): # false bc cannot have right bracket before a corresponding left bracket
                return False
            if rights.index(bracket) != lefts.index(bracket): # if index in the string isnt same, it is mismatched
                return False
    return stack.is_empty()