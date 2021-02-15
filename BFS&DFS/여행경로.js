function solution(tickets) {
    const answer = [];
    const n = tickets.length;
    const LENGTH = n + 1;
    const visit = new Array(n).fill(false);
    console.log(n);
    const queue = [];
    tickets.sort((a, b) => a[1].localeCompare(b[1]))

    for (let i = 0; i < n; i++) {
        if (tickets[i][0] === 'ICN') {
            visit[i] = true;
            queue.push([tickets[i][1], [tickets[i][0], tickets[i][1]], visit]);
            break;
        }
    }
    while (queue.length) {
        const [end, result, visit] = queue.shift();
        if (result.length === LENGTH) {
            answer.push(result);
        }
        for (let i = 0; i < n; i++) {
            if (tickets[i][0] === end && visit[i] === false) {
                const _visit = [...visit]
                _visit[i] = true;
                queue.push([tickets[i][1], [...result, tickets[i][1]], _visit]);
            }
        }
    }
    return answer[0];
}