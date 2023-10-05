
# Text to Number Encoding and Decoding Method

# Encoding and Decoding Functions
def encode(s):
    s = str(s)
    return sum(ord(s[i])*256**i for i in range(len(s)))

def decode(n):
    n = int(n)
    v = []
    while n != 0:
        v.append(chr(n % 256))
        n //= 256
    return ''.join(v)

# Functions to handle file input and output
def write_number_to_file(n, file_path):
    with open(file_path, 'w') as f:
        f.write(str(n))

def read_number_from_file(file_path):
    with open(file_path, 'r') as f:
        return int(f.read().strip())

# Example usage
if __name__ == '__main__':
    s = f"Horrible place, isn't it? said Kate"
    file_path = 'encoded_number.txt'
    
    n = encode(s)
    print('Encoded message:', n)
    write_number_to_file(n, file_path)
    
    n_from_file = read_number_from_file(file_path)
    s_decoded = decode(n_from_file)
    
    print('Decoded message:', s_decoded)
