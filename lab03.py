SBOX = [
    0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5, 0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7
]
SBOX_INV = [
    0xA, 0x5, 0x9, 0xB, 0x1, 0x7, 0x8, 0xF, 0x6, 0x0, 0x2, 0x3, 0xC, 0x4, 0xD, 0xE
]
MIX_COLUMN_MATRIX = [[1, 4], [4, 1]]

def add_key(s, k):
    return [si ^ ki for si, ki in zip(s, k)]

def sub_nibbles(sbox, s):
    return [sbox[si] for si in s]

def shift_rows(s):
    return [s[0], s[1], s[3], s[2]]

def mix_columns(s):
    return [
        s[0] ^ multiply(4, s[1]),
        s[1] ^ multiply(4, s[0]),
        s[2] ^ multiply(4, s[3]),
        s[3] ^ multiply(4, s[2])
    ]

def multiply(a, b):
    p = 0
    while b:
        if b & 0x1:
            p ^= a
        a <<= 1
        if a & 0x10:
            a ^= 0b10011
        b >>= 1
    return p & 0xF

def key_expansion(key):
    def nibble_swap(byte):
        return (byte & 0xF) << 4 | (byte >> 4)

    rcon = [0x80, 0x30]
    keys = [key >> 8, key & 0xFF]
    for i in range(2):
        temp = keys[-1]
        temp = nibble_swap(temp)
        temp = sub_nibbles(SBOX, [temp >> 4, temp & 0xF])
        temp = temp[0] << 4 | temp[1]
        temp ^= rcon[i]
        keys.append(keys[-2] ^ temp)
        keys.append(keys[-1] ^ keys[-2])
    return [(keys[2 * i] << 8) | keys[2 * i + 1] for i in range(3)]

def aes_round(s, k):
    s = sub_nibbles(SBOX, s)
    s = shift_rows(s)
    s = mix_columns(s)
    s = add_key(s, k)
    return s

def aes_final_round(s, k):
    s = sub_nibbles(SBOX, s)
    s = shift_rows(s)
    s = add_key(s, k)
    return s

def encrypt(plaintext, key):
    s = [(plaintext >> (i * 4)) & 0xF for i in range(4)]
    keys = key_expansion(key)
    s = add_key(s, [(keys[0] >> (i * 4)) & 0xF for i in range(4)])
    s = aes_round(s, [(keys[1] >> (i * 4)) & 0xF for i in range(4)])
    s = aes_final_round(s, [(keys[2] >> (i * 4)) & 0xF for i in range(4)])
    return sum([s[i] << (i * 4) for i in range(4)])

def decrypt(ciphertext, key):
    s = [(ciphertext >> (i * 4)) & 0xF for i in range(4)]
    keys = key_expansion(key)
    s = add_key(s, [(keys[2] >> (i * 4)) & 0xF for i in range(4)])
    s = shift_rows(s)
    s = sub_nibbles(SBOX_INV, s)
    s = add_key(s, [(keys[1] >> (i * 4)) & 0xF for i in range(4)])
    s = mix_columns(s)
    s = shift_rows(s)
    s = sub_nibbles(SBOX_INV, s)
    s = add_key(s, [(keys[0] >> (i * 4)) & 0xF for i in range(4)])
    return sum([s[i] << (i * 4) for i in range(4)])

plaintext = 0b1100110001011100
key = 0b0100111011110111
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print(f"Plaintext: {bin(plaintext)[2:].zfill(16)}")
print(f"Ciphertext: {bin(ciphertext)[2:].zfill(16)}")
print(f"Decrypted Text: {bin(decrypted_text)[2:].zfill(16)}")
