hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
expected_flag_structure = "crypto{"

encrypted_data = bytes.fromhex(hex_string)

for key in range(256):
    decrypted_data = bytes([byte ^ key for byte in encrypted_data])
    if decrypted_data.startswith(expected_flag_structure.encode('utf-8')):
        print(f"Key: {key}, Decrypted Data: {decrypted_data.decode('utf-8')}")
