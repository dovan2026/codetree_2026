N = int(input())
lst = []

for i in range(1, N+1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        lst.append(i)

print(len(lst))