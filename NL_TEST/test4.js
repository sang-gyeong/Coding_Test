// 정사각형 격자 도시
function solution(N, bus_stop) {
    let answer = [[]];
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];
    const _stop = bus_stop.map(stop => [stop[0] - 1, stop[1] - 1]);
    let d = Array.from(Array(N), () => new Array(N).fill(0));

    for (let stop of _stop) {
        d[stop[0]][stop[1]] = -1;
    }

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            let found = false;
            if (d[i][j] === -1) continue;
            let visit = Array.from(Array(N), () => new Array(N).fill(false));
            visit[i][j] = true;
            let queue = [];
            queue.push([i, j, 0]);
            while (queue.length && found === false) {
                let [x, y, dist] = queue.shift();
                for (let k = 0; k < 4; k++) {
                    const nx = x + dx[k];
                    const ny = y + dy[k];

                    if (nx >= 0 && nx < N && ny >= 0 && ny < N && visit[nx][ny] === false) {
                        visit[nx][ny] = true;
                        if (d[x][y] === 0) dist += 1
                        else dist = Math.min(dist + 1, d[x][y] + 1);
                        if (d[nx][ny] === -1) {
                            if (d[i][j] === 0 || dist < d[i][j]) d[i][j] = dist;
                            found = true;
                            break;
                        }
                        queue.push([nx, ny, dist])
                    }
                }
            }
        }
    }
    for (let dist of d) {
        for (let ele of dist) {
            if (ele === -1) {
                ele = 0;
            } else {
                ele -= 1;
            }
        }
    }




    return d;
}