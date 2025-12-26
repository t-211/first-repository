N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
res = []
next = 0

for _ in range(N):
     next = (next + K - 1) % len(arr)
     res.append(arr.pop(next))
     
print(f"<{', '.join(map(str, res))}>")