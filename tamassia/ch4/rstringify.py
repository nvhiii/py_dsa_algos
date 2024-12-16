def recursive_stringify(string):
    if len(string) == 1:
        return int(string)
    else:
        return recursive_stringify(string[:-1]) * 10 + int(string[-1])
    
print(recursive_stringify("12345"))