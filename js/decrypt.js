/*****************************

Use: "H3ll0 W0rld!".decrypt()
=> "Hello World!"

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

String.prototype.decrypt = function () {
	let out = this
	for (let i in l33t) {
		const reg = new RegExp(l33t[i].toString(), "gi")
		out = out.replace(reg, i)
	}
	return out
};

module.exports = text => text.decrypt()
