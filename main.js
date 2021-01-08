// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const solution = function(input) {
	input.shift();
	input.forEach(e => isNaN(e) ? e : parseInt(e))
	input.forEach(ele => {
		if (ele === 'd'){
			isEnqueue = false;
			if (queue.length === 0){
				console.log('underflow');
				return;
			}
			queue.shift();
		}else if (ele === 'e'){
			isEnqueue = true;
		}else {
			if (isEnqueue){
				isEnqueue = false;
				if (queue.length === MAX_SIZE){
					console.log('overflow');
					return;
				}
				queue.push(parseInt(ele));
			}else{
				return;
			}
		}
	})
}


const input = [];
const queue = [];
const MAX_SIZE = 10;
let count = 0;
let isEnqueue = false;

rl.on("line", function(line) {
	input.push(line);
	const n = parseInt(input[0]);
	if (line==='e') isEnqueue = true;
	else if (line ==='d' || isEnqueue){
		count++;
		isEnqueue = false;
	}
	if (count === n) rl.close();
}).on("close", function() {
	solution(input);
	console.log(queue.join(' '));
	process.exit();
});