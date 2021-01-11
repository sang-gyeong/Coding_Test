def solution(m, musicinfos):
    answer = "(None)"
    maxTime = 0
    m = transform(m)
    for info in musicinfos:
      [start, end, title, song] = info.split(',')
      [startMin, startSec] = start.split(':')
      [endMin, endSec] = end.split(':')
      song = transform(song)
      playTime = (int(endMin) * 60 + int(endSec)) - (int(startMin) * 60 + int(startSec))
      if playTime > len(song) :
        song = song*(playTime // len(song)) + song[:playTime%len(song)]
      else : song = song[:playTime]
      if m in song and maxTime < playTime:
        answer = title
        maxTime = playTime    
    return answer


def transform(m):
  sharp = ['C#', 'D#', 'F#', 'G#', 'A#']
  newSharp = ['ㅊ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅁ']

  for i in range(len(sharp)):
    if sharp[i] in m:
      m = m.replace(sharp[i], newSharp[i])
  
  return m
