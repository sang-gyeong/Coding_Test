const solution = mirror => {
    let answer = 0;
    const START_X = 7;
    const START_Y = 0;
    const dx = [1, -1, 0, 0, 0, -1, -1, 1, 1];
    const dy = [0, 0, 1, -1, 0, -1, 1, 1, -1];


    const q = [];
    q.push([START_X, START_Y, mirror]);

    while (q.length > 0 && answer !== 1) {
        let [x, y, mirror] = q.shift();
        if (mirror[x][y] === '#') continue;
        for (let k = 0; k < 9; k++) {
            let nx = x + dx[k];
            let ny = y + dy[k];
            if (nx >= 0 && nx < 8 && ny >= 0 && ny < 8 && mirror[nx][ny] !== '#') {
                if (nx < calTopWall(mirror) || calTopWall(mirror) === -1) {
                    answer = 1;
                    break;
                }
                q.push([nx, ny, copyMirror(mirror)]);
            }
        }
    }
    return answer
}

const calTopWall = (mirror) => {
    for (let i = 0; i < 8; i++) {
        if (mirror[i].includes('#')) {
            return i;
        }
    }
    return -1;
}


const copyMirror = (mirror) => {
    const _mirror = Array.from(Array(8), () => new Array(8).fill(0))

    for (let i = 1; i < 8; i++) {
        _mirror[i] = [...mirror[i - 1]];
    }
    _mirror[0] = new Array(8).fill('.')
    return _mirror;
}


const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: ""
});

const mirror = [];
rl.on("line", (line) => {
    mirror.push(line)
    if (mirror.length === 8) rl.close();
}).on("close", () => {
    console.log(solution(mirror));
    process.exit();
});