
// decode String
function solution(compressed) {
    let num_stack = [];
    let str_stack = [];
    let result = '';
    let n = compressed.length;
    for (let i = 0; i < n; i++) {
        let c = compressed.charAt(i);
        if (c === '(') {
            str_stack.push(result);
            result = '';
        } else if (c == ')') {
            let num = num_stack.pop();
            let tmp = str_stack.pop();
            for (let j = 0; j < num; j++) {
                tmp += result;
            }
            result = tmp;
        } else if (!isNaN(c)) {
            let num = Number(c);
            while (i + 1 < n && !isNaN(compressed.charAt(i + 1))) {
                num = num * 10 + Number(compressed.charAt(i + 1));
                i++;
            }
            num_stack.push(num);
        } else {
            result += c;
        }
    }
    return result;
}