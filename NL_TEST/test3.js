// 암호 알고리즘

function solution(encrypted_text, key, rotation) {
    const alphabet = '0abcdefghijklmnopqrstuvwxyz';
    const n = encrypted_text.length;
    let answer = '';
    let str = encrypted_text;
    if (rotation !== 0) {
        for (let i = 0; i < Math.abs(rotation); i++) {
            const isLeft = rotation > 0;
            str = rotate(str, isLeft);
        }
    }
    for (let i = 0; i < n; i++) {
        const s = str[i];
        const k = key[i];
        let index = alphabet.indexOf(s) - alphabet.indexOf(k);
        if (index <= 0) index += 26;
        answer += alphabet[index];
    }
    return answer;
}

const rotate = (str, isLeft) => {
    if (isLeft) {
        const first = str[0];
        return str.substring(1) + first;
    } else {
        const last = str[str.length - 1];
        return last + str.substring(0, str.length - 1);
    }
}