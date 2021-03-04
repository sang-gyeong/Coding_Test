# 16분 소요

# 풀이 : 딕셔너리를 사용해서 uid별 닉네임을 저장, 갱신하도록 함.
# 개선점 : 중복되는 코드

def solution(record):
    answer = []
    dic = {}
    enterMsg = '님이 들어왔습니다.'
    leaveMsg = '님이 나갔습니다.'
    
    for msg in record:
      words = msg.split()
      order = words[0]
      uid = words[1]
      if order == 'Enter' or order == 'Change':
        dic[uid] = msg.split()[2]
    
    for msg in record:
      words = msg.split()
      order = words[0]
      uid = words[1]
      if order == 'Enter':
        answer.append(dic[uid]+enterMsg)
      elif order == 'Leave':
        answer.append(dic[uid]+leaveMsg)
    return answer