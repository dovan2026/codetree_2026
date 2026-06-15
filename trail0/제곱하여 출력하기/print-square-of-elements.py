# 1. 데이터의 개수를 정수로 안전하게 입력받음
n = int(input())

# 2. 반복 변수명을 num으로 명확히 분리하고, 입력받은 개수(n)만큼만 슬라이싱
li1 = [int(num) for num in input().split()][:n]

# 3. 각 원소의 제곱 출력
for i in li1:
    print(i**2, end=' ')