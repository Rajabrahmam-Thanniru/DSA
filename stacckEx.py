s = "([(])"

brk = {
    '(': ')',
    '[': ']',
    '{': '}',
}

stack = []

for c in s:
    if c in brk:
        stack.append(c)
    else:
        if not stack:
            print(False)
            break
        curr = stack.pop()
        if c != brk[curr]:
            print(False)
            break
else:
    #
    if stack:
        print(False)
    else:
        print(True)
