k = int(input())

stack = []
result = 0

for _ in range(k):
    num = int(input())
    
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for i in stack:
    result += i
    
print(result)
    