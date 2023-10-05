
# Caesar Cipher Encoding and Decoding Method

# Caesar Cipher Encoding and Decoding Functions
def caesar_encode(s, k):
    s = str(s)
    n = sum(((ord(s[i]) + k) % 256)*256**i for i in range(len(s)))
    v = []
    while n != 0:
        v.append(chr(n % 256))
        n //= 256
    return ''.join(v)

def caesar_decode(s, k):
    s = str(s)
    n = sum((ord(s[i]) % 256)*256**i for i in range(len(s)))
    v = []
    while n != 0:
        m = ((n % 256) + 256 - k) % 256
        v.append(chr(m))
        n //= 256
    return ''.join(v)

# Functions to handle file input and output for Caesar Cipher
def write_caesar_to_file(v, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(v)

def read_caesar_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

# Example usage
if __name__ == '__main__':
    s = f'Between the roaring ocean and the endless canopy of heaven the flight of thoughts is indeed wonderful.'
    k = 7  # shift number
    file_path = 'caesar_ciphertext.txt'
    
    v = caesar_encode(s, k)
    print('Caesar Encoded Message:', v)
    write_caesar_to_file(v, file_path)
    
    v_from_file = read_caesar_from_file(file_path)
    s_decoded = caesar_decode(v_from_file, k)
    
    print('Caesar Decoded Message:', s_decoded)
