// 개미수열

function solution(n) {
    let answer = "";
    if (n === 1) return "1";
    answer = go(solution(n - 1));
    return answer;
}


function go(str) {
    let arr1 = [];
    let arr2 = [];
    let result = "";

    while (str.length) {
        if (str[0] === str[1]) {
            arr2.push(str[0]);
            str = str.replace(str[0], "");
        } else {
            arr2.push(str[0]);
            str = str.replace(str[0], "");
            arr1.push(arr2);
            arr2 = [];
        }
    }
    arr1.forEach(a => {
        result += `${a[0]}${a.length}`;
    })
    return result;
}
