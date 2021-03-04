function solution_1(array) { //통과
  const answer = [...array];
  answer.sort((a,b) => b-a)
  return answer;
}

function solution_2(a, b, c) {
  return (
      firstFunction(a) +
      secondFunction(b) +
      thirdFunction(c)
  );
}


function solution_3(text) {
  var answer = 0;
  var numIndexArr = [];
  for (let i=0; i<text.length; i++){
      if (text.charAt(i) === '1') numIndexArr.push(i);
  }
  numIndexArr.reduce((arr, cur)=> {
      answer = Math.max(answer, cur-arr)
      return cur
  })
  return answer;
}


function solution_7(a, b) {
  var answer = null;
  const sum = parseInt(a) + parseInt(b);
  answer = sum.toLocaleString('fullwide', {useGrouping:false});
  return answer + "";
}

//6
function solution(num) {
  return getData(num).then(getMax);
}

// DO NOT TOUCH BELOW CODE
function getData(num) {
  return Promise.resolve({
      first: 80 * num,
      second: 30 * num
  });
}

// DO NOT TOUCH BELOW CODE
function getMax(numbers) {
  return Promise.resolve(Math.max(...numbers));
}

// DO NOT TOUCH BELOW CODE
eval(function(p,a,c,k,e,d){e=function(c){return c};if(!''.replace(/^/,String)){while(c--){d[c]=k[c]||c}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('3.1.4("6"),3.1.5("7",0=>{14 2=8.13(0);12(2).11(0=>{9.10(0)})});',10,15,'s|stdin|o|process|setEncoding|on|utf8|data|JSON|console|log|then|solution|parse|var'.split('|'),0,{}))