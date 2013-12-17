import base58


def test_base_58_convert():
    """should take a long and convert it to base58Check format"""

    num = 0x100000
    actual = base58.base_58_convert(num)
    expected = "6Nhu"

    assert actual == expected

def test_count_leading_zero_bytes():
    """should find the number of leading zeros on a byte string"""

    bytes = "\x00\x00\x00\x12"
    actual = base58.count_leading_zero_bytes(bytes)
    expected = 3

    assert actual == expected

def test_decode():
    """should take a base58 encoded bitcoin address and return raw bytes for that address"""

    actual = base58.decode("14CAW1CobqYjs14boGNUwy5ZGNDRXjomFW")
    expected = "2304e21839bb9729ec18671893e4da55cb28a791".decode("hex")

    assert actual == expected

def test_encode():
    """should take a bitcoin address in raw byte format and encode it in base58"""

    actual = base58.encode("2304e21839bb9729ec18671893e4da55cb28a791".decode("hex"))
    expected = "14CAW1CobqYjs14boGNUwy5ZGNDRXjomFW"

    assert actual == expected