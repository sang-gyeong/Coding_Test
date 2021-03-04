// 약 한시간 소요 (첫 시도때는 풀지 못했는데, 이전 스터디에서 논의한 풀이법을 적용해서 풀 수 있었음) 
// 1. 후보키 속성 인덱스들의 모든 조합을 구하기
// 2. 앞에서부터 후보키 여부 판별, 후보키인 인덱스 조합을 제외시켜나가는 순서로 진행.
// 3. 후보키 여부 판별은 배열의 길이와 set의 길이 비교를 통해 가능.

// < 어려웠던 점 >
// 1. 파이썬-> 자바스크립트로 갈아타기
// 2. 일부 로직들을 함수로 분리할 필요가 있어보임.
// 3. 최소성 판별에서 애를 많이 먹었다. 처음에는 단순히 includes를 사용했는데
//  이 경우, 'ad'와 'abcd'를 걸러내지 못함.
//  => forEach로 순회 후 flag로 최소성 여부를 판별하도록 수정하였다.

function solution(relation) {
  let answer = 0;
  let hubo = [];
  const n = relation.length;
  const m = relation[0].length;
  const columns = [...new Array(m)].map((v, i) => i)
  for (let num of columns){
      let combinations = getCombinations(columns, num+1);
      for (let combination of combinations){
          let myArr = new Array(n).fill('');
          combination.forEach(c => {
              for (let i=0; i<n; i++){
                  myArr[i] += relation[i][c];
              }
          })
          let mySet = [...new Set(myArr)]
          if (mySet.length === n){
              hubo.push(combination.join(''));
          }
      }
  }
  let i = 0;
  while (i<hubo.length){
      for (let j=i+1; j<hubo.length; j++){
          let flag = true;
          hubo[i].split('').forEach(h => {
              if (!hubo[j].includes(h)){
                  flag = false;
              }
          })
          if (flag){
              hubo.splice(j, 1);
              j--;
          }
      }
      i++;
  }
  answer = hubo.length;
  return answer;
}

const getCombinations = function (arr, selectNumber) {
const results = [];
if (selectNumber === 1) return arr.map((value) => [value]); 
arr.forEach((fixed, index, origin) => {
  const rest = origin.slice(index + 1);
  const combinations = getCombinations(rest, selectNumber - 1); 
  const attached = combinations.map((combination) => [fixed, ...combination]); 
  results.push(...attached); 
});

return results;
}