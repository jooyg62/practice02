# 문제3.
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복 없이 각 단어를 순서대로 출력하세요.
# 2)각 단어의 빈도수도 함께 출력해 보세요

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.replace(',', '').replace('.', '').replace('\n', '')
l = s.split()
d = {}

for v in l:
    if d.get(v):
        d[v] += 1
    else:
        d[v] = 1

keys = d.keys()
for key in keys:
    print("{0}:{1}".format(key, d[key]))



