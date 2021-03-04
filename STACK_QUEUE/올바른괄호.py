# 소요 시간 : 22분

# 1. 올바른 괄호인지 판별하는 isRight 함수 - stack사용
# 2. u,v를 나누는 divide 함수 - open, close를 카운트하여 균형잡힌 괄호 판별
# 3. 두 함수를 사용하여 solution을 재귀적으로 구현


def solution(p):
  if isRight(p):
    return p
  u, v = divide(p)
  if isRight(u):
    return u + solution(v)
  else:
    str = '(' + solution(v) + ')'
    str = str + reverse(u[1:-1])
    return str

def reverse(u):
  result = ''
  for b in u:
    if b=='(':
      result = result + ')'
    else:
      result = result + '('
  return result

def isRight(p):
  stack = []
  for b in p:
    if len(stack)==0:
      stack.append(b)
    elif stack[-1]=='(' and b==')':
      stack.pop()
    else:
      stack.append(b)
  if len(stack)==0:
    return True
  else: 
    return False

def divide(p):
  open = 0
  close = 0
  for i in range(len(p)):
    if p[i]=='(':
      open+=1
    else:
      close+=1
    if open==close:
      return p[:i+1], p[i+1:]