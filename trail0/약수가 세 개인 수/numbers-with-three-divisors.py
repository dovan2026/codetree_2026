start, end = map(int, input().split())
lst_1 = []

for j in range(start, end+1):
    # 1. 매 숫자(j)마다 약수를 담을 리스트를 빈 상태로 초기화해야 합니다.
    lst = []
    
    # 2. 약수 검사는 end가 아닌, 현재 판별 중인 숫자 j까지만 진행합니다.
    for i in range(1, j+1):
        if j % i == 0:
            lst.append(i)
            
    # 3. j에 대한 약수를 끝까지 모두 찾은 후, 그 개수가 정확히 3개인지 확인합니다.
    if len(lst) == 3:
        lst_1.append(j)

print(len(lst_1))