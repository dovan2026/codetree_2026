N, M = input().split()

if len(N) > len(M):
    print(N, len(N))
elif len(N) == len(M):
    print('same')
elif len(N) < len(M):
    print(M, len(M))