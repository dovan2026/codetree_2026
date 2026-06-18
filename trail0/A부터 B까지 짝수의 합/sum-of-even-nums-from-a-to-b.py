N, M = map(int, input().split())
total = 0
for i in range(N, M+1):
    if i % 2 == 0:
        total += i
print(total)