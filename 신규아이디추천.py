import re
def solution(new_id):
    

    p = re.compile('[a-z0-9-_.]+')
    p2 = re.compile('[^.]+')
    answer = ''
    new_id = new_id.lower()
    new_id = "".join(p.findall(new_id))
    while ".." in new_id :
        new_id = re.sub('\.{2}', '.', new_id)
    if new_id == "." :
        new_id = ""
    while new_id != "" and (new_id[0] == '.' or new_id[-1] == '.') :
        if new_id[0] == '.' :
            new_id = new_id[1:]
        elif new_id[-1] == '.' :
            new_id = new_id[:-1]
    if new_id == "" :
        new_id = "a"
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        while new_id != "" and new_id[-1] == '.' :
            new_id = new_id[:-1]
    while len(new_id) < 3:
            new_id += new_id[-1]
    
    return new_id