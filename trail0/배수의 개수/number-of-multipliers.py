# 1. 세로로 입력되는 10개의 정수를 순서대로 읽어 리스트에 저장
lst = [int(input()) for _ in range(10)]

count_3 = 0
count_5 = 0

# 2. 리스트를 순회하며 3의 배수와 5의 배수를 각각 독립적으로 카운트
for num in lst:
    if num % 3 == 0:
        count_3 += 1
    if num % 5 == 0:
        count_5 += 1

# 3. 결과 출력 (예시: 5 5)
print(count_3, count_5)