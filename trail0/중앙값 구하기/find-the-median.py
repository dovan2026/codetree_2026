A, B, C = map(int, input().split())

if A > B:
    if C > A:
        print(A)
    elif C > B:
        print(C)
    else:
        print(B)
elif B > A:
    if C > B:
        print(B)
    elif C > A:
        print(C)
    else:
        print(A)
