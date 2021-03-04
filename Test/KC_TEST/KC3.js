// 74.1

function solution(next_student) {
  let answer = 0;
  let max_count = 0;
  const n = next_student.length;
  const student = next_student.map(s => s-1);
  
  for (let i=0; i<n; i++){
      let check = new Array(n).fill(false);
      let count = 1;
      check[i] = true;
      let target = student[i];
      while (target !== -1 && check[target] === false){
          count ++;
          check[target] = true;
          target = student[target];
      }
      if (count >= max_count){
          max_count = count;
          answer = i+1;
      }
  }
  return answer;
}