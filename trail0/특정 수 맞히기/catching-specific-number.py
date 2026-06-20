while True:
    x = int(input())
    if x < 25:
        print('Higher', end='\n')
    elif x > 25:
        print('Lower', end='\n')
    else:
        print('Good')
    
    if x == 25:
        break

