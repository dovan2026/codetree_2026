N = input()

lst = ['apple',
'banana',
'grape',
'blueberry',
'orange']

nums = 0
for i in range(len(lst)):
    if lst[i][2] == N or lst[i][3] == N:
        print(lst[i], end='\n')
        nums += 1
        

print(nums)