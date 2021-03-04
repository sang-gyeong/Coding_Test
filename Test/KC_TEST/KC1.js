// 모두통과
function solution(n, record) {
  let answer = [];
  let store = {};
  
  for (let rec of record){
      let [server, name] = rec.split(' ');
      if (store[server]) {
          if (store[server].includes(name)) continue;
          if (store[server].length === 5) store[server].shift();
          store[server].push(name);
      }
      else store[server] = [name];
  }
  for (let server in store){
      store[server].forEach(char => answer.push(char));
  }
  return answer;
}