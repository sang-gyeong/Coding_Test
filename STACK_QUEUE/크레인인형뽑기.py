def solution(board, moves):
  answer = 0
  basket = []
  n = len(board)

  for move in moves:
    j = move-1
    for i in range(n):
      doll = board[i][j]
      if doll != 0:
        if len(basket) != 0 and basket[-1] == doll:
          answer += 2
          basket.pop()
        else : basket.append(doll)
        board[i][j]=0
        break
  return answer
