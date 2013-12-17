import hashlib

BASE_58_DIGITS = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def byte_array_to_int(byte_array):
    return int(byte_array.encode('hex'), 16)


def base_58_lookup(index):
    return BASE_58_DIGITS[index]


def base_58_convert(num):
    b58 = []
    while num > 0:
        b58.append(base_58_lookup(num%58))
        num = num // 58

    return "".join(reversed(b58))


def count_leading_zero_bytes(bytes):
    count = 0
    position = 0
    while bytes[position] == '\x00':
        count += 1
        position += 1

    return count


def encode(payload):
    # step 1: concatenate version byte and payload
    version_payload = "".join(['\x00', payload])

    # step 2: find first four bytes of sha256 of step 1
    version_payload_hash = hashlib.sha256(hashlib.sha256(version_payload).digest()).digest()

    checksum = version_payload_hash[0:4]

    # step 3: concatenate the results of step 1 and 2
    version_payload_checksum = "".join([version_payload, checksum])

    # step 4: convert bytes into a single bignum and convert to base58

    bignum = byte_array_to_int(version_payload_checksum)

    b58 = base_58_convert(bignum)

    leading_zeroes = '1' * count_leading_zero_bytes(version_payload_checksum)

    return leading_zeroes + b58



def decode(b58_string):
    pass