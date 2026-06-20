N, M = map(int, input().split())
lst = [N]

while N <= M:
    if N % 2 == 1:
        N *= 2
    else:
        N += 3
    
    if N > M:
        break
    
    lst.append(N)

print(*lst)
