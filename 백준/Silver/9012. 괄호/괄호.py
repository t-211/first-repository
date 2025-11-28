N = int(input())

for _ in range(N):
    stack = []
    s = input()
    valid = True
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                valid = False
                break
    if stack:
        valid = False
    print("YES") if valid else print("NO")