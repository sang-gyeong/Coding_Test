
function solution(n, t, m, timetable) {
  let answer = '';
  const busTime = [...new Array(n)].map((v, i)=>540 + (t*i));
  const lastBus = busTime[busTime.length-1];
  const timeToMin = timetable.map(time => {
      const [hour, min] = time.split(':');
      return parseInt(hour) * 60 + parseInt(min);
  }).filter(time => time <= lastBus).sort((a,b)=>a-b);
  for (let i=0; i<busTime.length-1; i++){
      let count = 0;
      while (count < m && timeToMin.length > 0){
          if (timeToMin[0] <= busTime[i]){
              timeToMin.shift();
              count++;
          }else{
              break;
          }
      }
  }
  if (timeToMin.length < m){
      return minToTime(lastBus);
  }
  for (let i=timeToMin[0]-1; i<=lastBus; i++){
      const a = timeToMin.filter(t => t<=i);
      if (a.length >= m) {
          return minToTime(i-1);
      }
  }
}
function minToTime(minutes){
  const hour = Math.floor(minutes/60);
  const min = minutes - (hour * 60);
  return numToTime(hour) + ':' + numToTime(min);
}
function numToTime(num){
  return num < 10 ? '0' + String(num) : String(num);
}