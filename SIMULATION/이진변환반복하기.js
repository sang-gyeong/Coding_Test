function solution(s) {
  let answer = [0,0];
  let result = s;
  let count = 0;
  while (result !== '1'){
      let tmp = 0;
      result.split('').forEach(r => {
          if (r==='0') tmp++;
      })
      result = (result.length - tmp).toString(2);
      answer[1] += tmp;
      count ++;
  }
  answer[0] = count;
  return answer;
}