from pwn import xor

hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
expected_flag_structure = "crypto{"

encrypted_data = bytes.fromhex(hex_string)
encrypted_flag = bytes.fromhex(expected_flag_structure.encode("utf-8").hex())

dataXORFlag = bytes([a ^b for a,b in zip(encrypted_data, encrypted_flag)])

key = dataXORFlag.decode('utf-8') + str("y")
key = str.encode(key)

flag = xor(encrypted_data, key)
print(flag.decode('utf-8'))