from sys import getrecursionlimit, setrecursionlimit

old = getrecursionlimit()
new = setrecursionlimit(10000) # easiest way to bypass pythons default max recursion depth, for valid calculations