function solution(genres, plays) {
    const answer = [];
    const result = [];
    const n = genres.length;
    const store = {};
    for (let index = 0; index < n; index++) {
        const init = [index, plays[index]];
        if (store[genres[index]]) {
            store[genres[index]][0] += parseInt(plays[index]);
            store[genres[index]][1].push(init);
        } else {
            store[genres[index]] = [parseInt(plays), [init]];
        }
    }
    for (let genre in store) {
        result.push(store[genre]);
    }
    result.sort((a, b) => b[0] - a[0]);

    for (let store of result) {
        let count = 0;
        const arrs = store[1];
        arrs.sort((a, b) => b[1] === a[1] ? a[0] - b[0] : b[1] - a[1]);
        for (let album of arrs) {
            count += 1;
            answer.push(album[0]);
            if (count === 2) break;
        }
    }
    return answer;
}