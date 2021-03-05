import re


def solution(new_id):
    st = new_id.lower()
    st = re.sub('[^a-z0-9\-_.]+', '', st)
    st = re.sub('\.{2,}', '.', st)
    st = re.sub('^\.|\.$', '', st)
    st = st if len(st) > 0 else 'a'
    st = st if len(st) < 16 else st[:15]
    st = re.sub('\.$', '', st)
    st = st if len(st) > 2 else st + st[-1] * (3-len(st))

    return st


p = re.compile('[a-z]', re.I)
m = p.match('python')
print(m)

m = p.match('Python')
print(m)

m = p.match('PYTHON')
print(m)
