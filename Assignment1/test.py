def chacha_quarter_round(a, b, c, d):
    a = (a + b) & 0xFFFFFFFF
    d = (d ^ a) & 0xFFFFFFFF
    d = (d << 16 | d >> 16) & 0xFFFFFFFF
    c = (c + d) & 0xFFFFFFFF
    b = (b ^ c) & 0xFFFFFFFF
    b = (b << 12 | b >> 20) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    d = (d ^ a) & 0xFFFFFFFF
    d = (d << 8 | d >> 24) & 0xFFFFFFFF
    c = (c + d) & 0xFFFFFFFF
    b = (b ^ c) & 0xFFFFFFFF
    b = (b << 7 | b >> 25) & 0xFFFFFFFF
    return a, b, c, d

def chacha_double_round(state):
    state[0], state[4], state[8], state[12] = chacha_quarter_round(state[0], state[4], state[8], state[12])
    state[1], state[5], state[9], state[13] = chacha_quarter_round(state[1], state[5], state[9], state[13])
    state[2], state[6], state[10], state[14] = chacha_quarter_round(state[2], state[6], state[10], state[14])
    state[3], state[7], state[11], state[15] = chacha_quarter_round(state[3], state[7], state[11], state[15])
    state[0], state[5], state[10], state[15] = chacha_quarter_round(state[0], state[5], state[10], state[15])
    state[1], state[6], state[11], state[12] = chacha_quarter_round(state[1], state[6], state[11], state[12])
    state[2], state[7], state[8], state[13] = chacha_quarter_round(state[2], state[7], state[8], state[13])
    state[3], state[4], state[9], state[14] = chacha_quarter_round(state[3], state[4], state[9], state[14])
    return state

def chacha_block(key, nonce, counter):
    constants = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]
    state = constants + key + [counter & 0xFFFFFFFF, (counter >> 32) & 0xFFFFFFFF] + nonce
    working_state = state[:]
    for _ in range(10):
        working_state = chacha_double_round(working_state)
    for i in range(16):
        working_state[i] = (working_state[i] + state[i]) & 0xFFFFFFFF
    return b''.join(x.to_bytes(4, byteorder='little') for x in working_state)

def chacha_encrypt(key, nonce, plaintext):
    counter = 0
    ciphertext = b''
    while len(plaintext) > 0:
        key_stream = chacha_block(key, nonce, counter)
        counter += 1
        chunk_size = min(len(plaintext), 64)
        ciphertext += bytes(p ^ k for p, k in zip(plaintext[:chunk_size], key_stream[:chunk_size]))
        plaintext = plaintext[chunk_size:]
    return ciphertext

# Example usage:
if __name__ == "__main__":
    key = [
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
        0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f
    ]
    nonce = [0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x4a, 0x00, 0x00, 0x00, 0x00]
    plaintext = b"Aa15602809798"

    ciphertext = chacha_encrypt(key, nonce, plaintext)
    print("Ciphertext:", ciphertext.hex())