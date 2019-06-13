# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
def printlist(l):
    try:
        l.remove('')
    except ValueError:
        pass

    for i in range(0, len(l)):
        l[i] = "'" + l[i] + "'"

    print(', '.join(l))


s = '/usr/local/bin/python'

# 디렉토리 경로명을 분리해서 출력
l = s.split('/')
printlist(l)

# 디렉토리 경로명과 파일명을 분리하여 출력
l = s.rsplit('/', 1)
printlist(l)



