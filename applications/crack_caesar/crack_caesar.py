# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# get Key
decode_table = {}
frequency = {}
def build_decode_table():
    for key, value in encode_table.items():
        decode_table[value] = key

def encode(s):
    ctext = open('ciphertext.txt', 'r')
    ciphtext = ctext.read()
    type(ctext)
    for c in s:
        if c in encode_table:
            r += encode_table[c]
        else:
            r += c
    return r
​
def decode(s):
    r = ""
    for c in s:
        if c in decode_table:
            r += decode_table[c]
        else:
            r += c
    return r
​
build_decode_table()
​
print(encode("HELLO, WORLD!"))
​
print(decode("DOGGE, BEUGW!"))
​
​
​


