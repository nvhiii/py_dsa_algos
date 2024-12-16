from arraystack import ArrayStack

def matched(expr):
    lefts = "{(["
    rights = "})]"
    stack = ArrayStack()
    for char in expr:
        if char in lefts:
            stack.push(char)
        elif char in rights:
            if stack.is_empty(): # false bc cannot have right bracket before a corresponding left bracket
                return False
            if rights.index(char) != lefts.index(char): # if index in the string isnt same, it is mismatched
                return False
    return stack.is_empty()