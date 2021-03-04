function solution(n, computers) {
  let answer = 0;
  const isVisit = [...new Array(n)].fill(false);
  
  function dfs(index){
      isVisit[index] = true;
      
      for(let i = 0; i< n; i++ ){
          if(computers[index][i] === 1 && !isVisit[i]){
              dfs(i);
          }
      }
  }
  for(let  i = 0;  i < n; i++ ){
      if(!isVisit[i]){
          dfs(i);
          answer+=1;
      }
  }   
  return answer;
}