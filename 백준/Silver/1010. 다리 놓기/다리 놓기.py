import math

count = int(input())
for _ in range(count):
    n, m = map(int, input().split())
    print(math.comb(m, n))
