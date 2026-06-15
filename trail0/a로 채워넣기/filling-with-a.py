str = input()
str = list(str)

str[1] = 'a'
str[-2] = 'a'

print(*str, sep = '')