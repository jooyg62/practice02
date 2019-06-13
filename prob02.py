# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
                To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

while True:
    start_tag = s.find('<')
    end_tag = s.find('>')

    if start_tag == -1 or end_tag == -1:
        break

    # 제거할 단어 선택
    delstr = s[start_tag:end_tag+1]
    s = s.replace(delstr, '')

print(s)

