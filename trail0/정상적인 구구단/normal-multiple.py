N = int(input())

for i in range(1, N+1):
    for j in range(1, N+1):
        if j == N:
            # 마지막 열(N번째)일 때는 쉼표 없이 기본 줄바꿈
            print(f'{i} * {j} = {i*j}', sep='')
        else:
            # 마지막 열이 아닐 때만 쉼표 추가, 줄바꿈 방지
            print(f'{i} * {j} = {i*j}', end=', ')