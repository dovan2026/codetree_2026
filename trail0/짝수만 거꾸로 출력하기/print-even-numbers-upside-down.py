N = int(input())

lst = [int(M) for M in input().split()][:N]
lst_1 = []

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        lst_1.append(lst[i])

print(*lst_1[::-1])