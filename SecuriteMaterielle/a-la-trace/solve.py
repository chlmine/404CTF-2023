cipher = [0x49,0xb7,0x71,0x9f,0x90,0xcc,0x74,0x9f,0xca,0xa4,0x64,0xb9,0x83,0x7a,0x9e,0x5e]
flag = chr(cipher[0])

for i in range(1, len(cipher)):
    flag += chr((cipher[i] - ord(flag[i - 1])) ^ ord(flag[i - 1]))

print(f'404CTF{{{flag}}}')