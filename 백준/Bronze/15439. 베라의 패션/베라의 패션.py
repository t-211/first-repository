N = int(input())

top = [i for i in range(N)]
pants = [i for i in range(N)]

count = 0

for t in top:
    for p in pants:
        if t != p:
            count += 1
            
print(count)