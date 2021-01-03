def solution(s):
    answer = len(s)
    count = 0
    target = ''

    for length in range(1, (len(s)//2)+1):
      target = s[0:length]
      overlap = 1
      count = 0
      for i in range(length, len(s), length):
        print('i :',i)
        current = s[i : i+length]
        print(target, current)
        if target == current:
          overlap += 1
          if (i+length >= len(s)):
            count += (overlap//10)+1
            count += len(target)
            current = ''
        else:
          if overlap > 1:
            count += (overlap//10)+1
            print('자릿수 : ', (overlap//10)+1)
          count += len(target)
          overlap = 1
          target = current
      count += len(current)
      count += len(s)%length
      print('count :', count)
      if answer > count:
        answer = count
    
    return answer