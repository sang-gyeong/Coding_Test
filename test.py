def solution(s):
    answer = len(s)
    for length in range(1, (len(s)//2)+1):
      count = 0
      arr = []
      for i in range(0, len(s), length):
        arr.append(s[i:i+length])
        target = arr[0]
        overlap = 1
      arr.append('')
      for i in range(1, len(arr)):
        current = arr[i]
        if target == current:
          overlap += 1
        else:
          if overlap > 1:
            count += (overlap//10) + 1
          count += len(target)
          target = current
          overlap = 1
      count += len(current)
      if answer > count:
        answer = count
    
    return answer