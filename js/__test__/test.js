// Test made using EyeJS - https://eye.js.org

const path = require('path').normalize(__testDir + "/../")

const { encrypt, decrypt } = require(path + "lib.js")

eye.test("Encryption", "node",
	$ => $(encrypt("Hello World!")).Equal("H3ll0 W0rld!"),
	$ => $(encrypt("LEETLANGUAGE")).Equal("L337L4N6U463")
)
eye.test("Decryption", "node",
	$ => $(decrypt("H3ll0 W0rld!")).Equal("Hello World!"),
	$ => $(decrypt(encrypt("CrypTools"))).Equal("Cryptools") // 'T' becomes 't', because T = t = 7 
)
