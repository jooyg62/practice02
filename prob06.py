import random
import sys

min, max = 1, 100

n = random.randrange(max) + min
print('수를 결정하였습니다. 맞추어 보세요')
print('1-100')
# print('정답: ', n)
cnt = 0

while True:
    cnt += 1
    value = int(input(str(cnt) + '>> '))


    if n == value:
        print('맞았습니다.')

        if 'y' != input('다시 하시겠습니까?(y/n) >> '):
            break
        else:
            n = random.randrange(max) + min
            cnt = 0
            # print('정답: ', n)
            continue
    elif n > value:
        print('더 높게')
    elif n < value:
        print('더 낮게')
    else:
        print('예외 발생')
        sys.exit(0)

