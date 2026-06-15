N, M = map(int, input().split())

lst = [N, M]
a = lst[-1]

for i in range(8):
    a += lst[-2]
    a = a % 10
    lst.append(a)

print(*lst)