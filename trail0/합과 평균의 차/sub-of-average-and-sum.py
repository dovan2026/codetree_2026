a, b, c = map(int, input().split())

total = a + b + c
avg = total // 3

print(f"{total}\n{avg}\n{total - avg}")