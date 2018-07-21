"""
Each Morse code character is represented by a series of "dots" and "dashes". In binary,
a dot is a single bit (1) and a dash is three bits (111). Between each dot or dash
within a single character, we place a single zero bit. (I.e. "dot dash" would become 10111.)
Separate characters are separated by three zero bits (000). Words are spearated by a single
space, which is represented by 7 zero bits (0000000).

The first method Morse.encode will take a String representing the message and will return an
array of signed 32-bit integers in big-endian order and in two's complement format.
(Note: This is the standard format for numbers returned by JavaScript bitwise operators.)
Since it is possible that the Morse encoded message will not align perfectly with
the binary 32-bit numbers, all unused bits are to be padded with 0's.

The second method Morse.decode will take an array of numbers and return the String representation
of the message.
"""


class Morse:
    @staticmethod
    def bytes_converter(data):
        if isinstance(data, str):
            integer = int(data, base=2)
            return int.from_bytes(integer.to_bytes(4, byteorder='big'), byteorder='big', signed=True)
        elif isinstance(data, int):
            integer = data
            try:
                result = bin(int.from_bytes(integer.to_bytes(4, 'big', signed=True), 'big'))[2:]
            except OverflowError:
                result = bin(int.from_bytes(integer.to_bytes(4, 'big', signed=False), 'big'))[2:]
            if result != 32:                                    # Since bin() strips the highest insignificant bites
                result = '0' * (32 - len(result)) + result
            return result

    # @classmethod                                      # For Python 2.X
    # def translate(cls, word):
    #     newword = ''
    #     for char in word:
    #         newword += cls.alpha[char]
    #     return newword

    @classmethod
    def wordmaker(cls, code):
        word = ''
        for char in code.split('000'):
            # print('CHAR:', char)
            char = char.rstrip('0')
            for key, value in cls.alpha.items():
                if char == value:
                    # print('KEY:', key)
                    word += key
        return word

    @classmethod
    def encode(cls, message):
        output = []
        table = str.maketrans(cls.alpha)
        words = message.split()                             # Extract words
        words = ['   '.join(word) for word in words]        # Add 3 spaces between chars in every word
        words = [word.translate(table) for word in words]   # Translate every word
        # words = [cls.translate(word) for word in words]
        # print(words)
        result = '0000000'.join(words)                      # Join translated words by using 7 zeroes
        while result:
            block, result = result[:32], result[32:]
            if block != 32:
                block = block + '0' * (32 - len(block))     # Add zeroes to the end if length less than 32
            output.append(cls.bytes_converter(block))
        return output

    @classmethod
    def decode(cls, codes):
        message = ''
        for code in codes:
            # print('CODE:', code)
            # print('DECODED:', cls.bytes_converter(code))
            message = message + cls.bytes_converter(code)
        words = message.split('0000000')
        # print('WORDS:', words)
        words = [cls.wordmaker(code) for code in words if cls.wordmaker(code) != '']
        return (' '.join(words)).strip()

    alpha = {
      'A': '10111',
      'B': '111010101',
      'C': '11101011101',
      'D': '1110101',
      'E': '1',
      'F': '101011101',
      'G': '111011101',
      'H': '1010101',
      'I': '101',
      'J': '1011101110111',
      'K': '111010111',
      'L': '101110101',
      'M': '1110111',
      'N': '11101',
      'O': '11101110111',
      'P': '10111011101',
      'Q': '1110111010111',
      'R': '1011101',
      'S': '10101',
      'T': '111',
      'U': '1010111',
      'V': '101010111',
      'W': '101110111',
      'X': '11101010111',
      'Y': '1110101110111',
      'Z': '11101110101',
      '0': '1110111011101110111',
      '1': '10111011101110111',
      '2': '101011101110111',
      '3': '1010101110111',
      '4': '10101010111',
      '5': '101010101',
      '6': '11101010101',
      '7': '1110111010101',
      '8': '111011101110101',
      '9': '11101110111011101',
      '.': '10111010111010111',
      ',': '1110111010101110111',
      '?': '101011101110101',
      "'": '1011101110111011101',
      '!': '1110101110101110111',
      '/': '1110101011101',
      '(': '111010111011101',
      ')': '1110101110111010111',
      '&': '10111010101',
      ':': '11101110111010101',
      ';': '11101011101011101',
      '=': '1110101010111',
      '+': '1011101011101',
      '-': '111010101010111',
      '_': '10101110111010111',
      '"': '101110101011101',
      '$': '10101011101010111',
      '@': '10111011101011101',
      ' ': '0'}


if __name__ == '__main__':

    # HELLO WORLD encode/decode
    string = 'HELLO WORLD'
    print(Morse.encode(string))
    codes = [-1440552402, -1547992901, -1896993141, -1461059584]
    print(Morse.decode(codes))

    # MMM encode
    code1 = [-298086688]
    print(Morse.decode(code1))
    code2 = [3996880608]
    print(Morse.decode(code2))

    # EEEEEEEIE encode/decode
    code3 = [-2004318070, 536870912]
    print(Morse.decode(code3))
    string2 = 'EEEEEEEIE'
    print(Morse.encode(string2))

    # Complex string encode/decode
    string = 'XYWAI3D3IE $@PYL !"K7GF'
    print(Morse.encode(string))

    codes = [-354177310, -298964821, -1192613138, 679521195, -1950684997,
             -1548819734, 61782923, -1415336389, -1438932294]
    print(Morse.decode(codes))
