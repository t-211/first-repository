n = int(input())
line = list(map(int, input().split()))
stack = []
t = 1

for i in line:
    stack.append(i)
    while stack and stack[-1] == t:
        stack.pop()
        t += 1

if stack:
    print("Sad")
else:
    print("Nice")