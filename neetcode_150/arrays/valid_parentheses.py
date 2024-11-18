def valid_parentheses(s: list):
    stack = []
    cto = {")" : "(", "]" : "[", "}" : "{"}
    for c in s:
        if c in cto:
            if stack and s[-1] == cto[c]: # while stack isnt empty and if bracket pair is matching open and close
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    # outlier case for is s is empty
    return True if not stack else False