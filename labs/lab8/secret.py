def encode(message, key):
    acc = ' '
    for c in message:
        i = ord(c)
        new_char = chr(i + key)
        acc = acc + new_char
    return acc
