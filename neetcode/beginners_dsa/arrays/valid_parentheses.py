def valid_parentheses(s: list):
    stack = []
    cto = {")" : "(", "]" : "[", "}" : "{"}
    
    # while or for
    for c in s:
        if c in cto:
            if stack and cto[c] == stack[-1]: # check if stack exists, and check if both are same
                stack.pop()
            else:
                return False # return False bc nonmatching or stack empty
        else: # we append char to stack
            stack.append(c)

    # outlier case
    return True if not stack else False