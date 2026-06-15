N = int(input())
list_M = []

for i in range(N):
    try:
        row = list(map(int, input().split()))
        squared_row = [num ** 2 for num in row]
        list_M.append(squared_row)
    except EOFError:
        # 읽을 입력이 더 이상 없으면 에러를 내지 않고 루프를 종료
        break

print(*list_M[0])