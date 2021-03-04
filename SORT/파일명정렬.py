# 38분 소요

# 1. re 라이브러리를 사용하여 number 추출.
# 2. 대문자로 변환한 header, int로 변환한 number를 넣은 튜플 리스트 생성.
# 3. 람다식을 사용하여 header, number 순으로 튜플 리스트를 정렬함.
# (+) number가 5자리 이상일경우에 대한 예외처리가 필요함.

import re

def solution(files):
    newArr = []
    for file in files:
      numbers = re.findall("\d+", file)
      head = file.split(numbers[0])[0].upper()
      number = int(numbers[0])
      newArr.append((file, head, number))
    sortedArr = sorted(newArr, key = lambda x : (x[1], x[2]))
    answer = []
    for a in sortedArr :
      answer.append(a[0])
    return answer