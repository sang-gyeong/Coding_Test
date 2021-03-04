function solution(progresses, speeds) {
  const times = [];
  const answer = [];
  for (let i=0; i<progresses.length; i++){
      times.push(Math.ceil((100-progresses[i])/speeds[i]));
  }
  let target = times[0];
  let count = 0;
  for (let time of times){
      if (time>target){
          answer.push(count)
          count = 1;
          target = time;
      }else{
          count++;
      }
  }
  answer.push(count)

  return answer;
}