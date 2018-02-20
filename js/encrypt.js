/*****************************

Use: "Hello World!".encrypt()
=> "H3ll0 W0rld!"

*****************************/

const l33t = {
    "a": 4,
    "e": 3,
    "g": 6,
    "i": 1,
    "o": 0,
    "s": 5,
    "t": 7,
    "A": 4,
    "E": 3,
    "G": 6,
    "I": 1,
    "O": 0,
    "S": 5,
    "T": 7
}

String.prototype.encrypt = function () {
	let out = this
	for (let i in l33t) {
		const reg = new RegExp(i, "gi")
		out = out.replace(reg, l33t[i].toString())
	}
	return out
};

module.exports = text => text.encrypt()
