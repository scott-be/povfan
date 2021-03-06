#!/usr/bin/env python

from sys import argv

class IntelFan:
    asciitable = {
        'A': [0x40, 0x37, 0x37, 0x37, 0x40],
        'B': [0x49, 0x36, 0x36, 0x36, 0x00],
        'C': [0x3E, 0x3E, 0x3E, 0x3D, 0x63],
        'D': [0x63, 0x5D, 0x3E, 0x3E, 0x00],
        'E': [0x3E, 0x36, 0x36, 0x36, 0x00],
        'F': [0x3F, 0x37, 0x37, 0x37, 0x00],
        'G': [0x30, 0x36, 0x36, 0x3D, 0x00],
        'H': [0x00, 0x77, 0x77, 0x77, 0x00],
        'I': [0x7F, 0x3E, 0x00, 0x3E, 0x7F],
        'J': [0x3F, 0x00, 0x3E, 0x3E, 0x7C],
        'K': [0x3E, 0x5D, 0x6B, 0x77, 0x00],
        'L': [0x7E, 0x7E, 0x7E, 0x7E, 0x00],
        'M': [0x00, 0x4F, 0x67, 0x4F, 0x00],
        'N': [0x00, 0x78, 0x63, 0x4F, 0x00],
        'O': [0x41, 0x3E, 0x3E, 0x3E, 0x41],
        'P': [0x4F, 0x37, 0x37, 0x37, 0x00],
        'Q': [0x44, 0x39, 0x3A, 0x3E, 0x41],
        'R': [0x1C, 0x2B, 0x37, 0x37, 0x00],
        'S': [0x39, 0x36, 0x36, 0x36, 0x4E],
        'T': [0x3F, 0x3F, 0x00, 0x3F, 0x3F],
        'U': [0x00, 0x7E, 0x7E, 0x7E, 0x00],
        'V': [0x1F, 0x63, 0x7C, 0x63, 0x1F],
        'X': [0x1C, 0x6B, 0x77, 0x6B, 0x1C],
        'W': [0x00, 0x7C, 0x71, 0x7C, 0x00],
        'Y': [0x0F, 0x67, 0x70, 0x67, 0x0F],
        'Z': [0x9E, 0x8E, 0xA6, 0xB0, 0xB8],
        '!': [0xFF, 0xFF, 0x82, 0xFF, 0xFF],
        '@': [0xE7, 0xDB, 0xED, 0xDB, 0xE7], # Heart
        '*': [0x47, 0x3B, 0x5D, 0x3B, 0x47], # Big Heart
        '%': [0xF3, 0xDD, 0xFD, 0xDD, 0xF3], # Smiley Face
        '>': [0xBE, 0xDD, 0xEB, 0xF7, 0xFF],
        '<': [0xF7, 0xEB, 0xDD, 0xBE, 0xFF],
        ':': [0xFF, 0xFF, 0xDD, 0xFF, 0xFF],
        ' ': [0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    }

    def ascii2bin(self,string_array):
        blob = chr(len(string_array))

        for string in string_array:
            blob += chr(len(string))
            blob += self.string2bin(string)
        return blob


    def string2bin(self,string):
        strblob = ""

        for char in string.upper()[::-1]:
            if self.asciitable.has_key(char):
                for byte in self.asciitable[char]:
                    strblob += chr(byte)
            else:
                raise Exception, "Invalid character: '%s'" % byte
        return strblob


if __name__ == "__main__":
    for i in argv[1:]:
        if len(i) > 20:
            print "String to big (max = 20 chars)"
        else:
            print IntelFan().ascii2bin(argv[1:])
