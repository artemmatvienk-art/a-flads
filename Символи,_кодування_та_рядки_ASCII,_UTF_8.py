text = "bike"
shift = 12

encrypted = ""

for char in text:
    code = ord(char)
    new_code = (code - ord('a') + shift) % 26 + ord('a')
    encrypted += chr(new_code)

    print("Зашифрований текст:", encrypted)
