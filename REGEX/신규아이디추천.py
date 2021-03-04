import re 
def solution(new_id):
    # 1
    st = new_id.lower()
    # 2
    st = re.sub('[^a-z0-9\-_.]+', '', st)
    # 3
    st = re.sub('\.{2,}', '.', st)
    # 4
    st = re.sub('^\.|\.$', '', st)
    # 5
    st = st if len(st) > 0 else 'a'
    # 6
    st = st if len(st) < 16 else st[:15]
    st = re.sub('\.$', '', st)
    # 7
    st = st if len(st) > 2 else st + st[-1] * (3-len(st))
    
    return st