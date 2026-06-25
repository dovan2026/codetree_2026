N = int(input()) 

for j in range(N):
    # 1. 매 회차마다 새로운 a, b 구간을 입력받음
    a, b = map(int, input().split())
    
    # 2. 매 회차마다 새로운 합을 구해야 하므로 여기서 0으로 초기화
    nums = 0
    
    for i in range(a, b+1):
        if i % 2 == 0:
            nums += i
            
    # 3. 해당 회차의 짝수 합계 출력 (불필요한 sep 제거)
    print(nums)