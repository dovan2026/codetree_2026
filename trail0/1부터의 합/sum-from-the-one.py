N = int(input())
num = 0
for i in range(1,N+1):
    num += i
    if num >= N:
        print(i)
        break