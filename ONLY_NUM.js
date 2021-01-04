// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const solution = function(input) {
	const n = parseInt(input.shift());
	const arr = input[0].split(' ').map(e => parseInt(e));
	const num = [];
	arr.forEach((e) => {
		num.includes(e) ? num.splice(num.indexOf(e), 1) : num.push(e)
	})
	console.log(num[0]);
}

const input = [];
rl.on("line", function(line) {
	input.push(line);
	if (input.length == 2){
		rl.close();
	}
}).on("close", function() {
		solution(input);
		process.exit();	
});

