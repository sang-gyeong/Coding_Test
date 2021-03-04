# 29분 26초

# 1. while문을 사용하여 튜브에게 필요한 길이만큼(t*m이하) 정답숫자를 구한다.
# 2. 정답숫자를 구하는 과정에서 convert 함수를 별도로 생성.
# 3. 정답숫자에서 튜브에게 필요한 숫자만 골라 출력한다.

def solution(n, t, m, p):
    answer = ''
    number = ''
    i=0
    while len(number) < t*m:
      number += convert(i, n)
      i = i+1
    for i in range(t):
        answer+= number[(i*m)+(p-1)]
    return answer

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]