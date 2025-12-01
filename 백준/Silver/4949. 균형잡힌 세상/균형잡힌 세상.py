while(1):
    s = input()
    stack = []
    
    if s == '.':
        break
    
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if stack:
        print("no")
    else:
        print("yes")