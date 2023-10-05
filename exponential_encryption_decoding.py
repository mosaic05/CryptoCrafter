
# Exponential (Diffie-Hellman) Encryption and Decoding Method

# Exponential Encryption and Decoding Functions
def exp_encode(P, e, p):
    return pow(P, e, p)

def exp_decode(C, d, p):
    return pow(C, d, p)

# Functions to handle file input and output for Exponential Encryption
def write_exp_to_file(C, file_path):
    with open(file_path, 'w') as f:
        f.write(str(C))

def read_exp_from_file(file_path):
    with open(file_path, 'r') as f:
        return int(f.read().strip())

# Example usage
if __name__ == '__main__':
    p = 23  # a prime number
    e = 5   # another prime number such that gcd(e, p-1) = 1

    # Calculate the multiplicative inverse of e modulo (p-1) for decryption
    d = pow(e, -1, p-1)

    P = 12  # plaintext number, should be less than p
    file_path = 'exp_ciphertext.txt'
    
    C = exp_encode(P, e, p)
    print('Exponential Encoded Cipher Text:', C)
    write_exp_to_file(C, file_path)
    
    C_from_file = read_exp_from_file(file_path)
    P_decoded = exp_decode(C_from_file, d, p)
    
    print('Exponential Decoded Cipher Text:', P_decoded)
