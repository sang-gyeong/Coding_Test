// 모두 통과.
function solution(m, v) {
  let answer = 0;
  let stack = [];

  for (let b_len of v){
    let point = -1;
    for (let i=stack.length-1; i>=0; i--){
      if (stack[i]>=b_len) point = i;
      else break;
    }
    if (point === -1) stack.push(m-b_len);
    else stack[point] -= b_len;
  }
  answer = stack.length;

  return answer;
}