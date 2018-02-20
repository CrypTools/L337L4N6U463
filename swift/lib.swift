/********************************
 
 Use: "Hello World!".encrypt
 => "H3ll0 W0rld!"
      "H3ll0 W0rld!".decrypt
 => "Hello World!"
 
 *******************************/

import Foundation

let l33t = [
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
]
extension String {
    var encrypt: String {
        var out = self
        for (l, n) in l33t {
            out = out.replacingOccurrences(of: l, with: String(n), options: .literal, range: nil)
        }
        return out
    }
    var decrypt: String {
        var out = self
        for (l, n) in l33t {
            out = out.replacingOccurrences(of: String(n), with: l, options: .literal, range: nil)
        }
        return out
    }
}
