stack = []

stack.append(1)
stack.append(2)
stack.append(3)
n = len(stack)
print(stack[n-1])
while stack:
    print(stack.pop())