text = input().split()
result = ""

for t in text:
    result = t + result  # 가져온 문자를 기존 결과물 앞쪽에 붙임

print(result)