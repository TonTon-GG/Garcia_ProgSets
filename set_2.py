def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        initial_pos = ord(letter) - ord("A")
        new_pos = (initial_pos + shift) % 26
        new_char = chr(new_pos + ord("A"))
        return new_char

def caesar_cipher(message, shift):
    new_msg = ""
    for letter in message:
        new_msg += shift_letter(letter, shift)
    return new_msg

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    else:
        initial_pos = ord(letter) - ord("A")
        shift = ord(letter_shift) - ord("A")
        new_pos = (initial_pos + shift) % 26
        new_char = chr(new_pos + ord("A"))
        return new_char

def vigenere_cipher(message, key):
    extn_key = (key * ((len(message) // len(key)) + 1))[:len(message)]
    enc_msg = []

    key_index = 0
    for letter in message:
        if letter == " ":
            enc_msg.append(letter)
            key_index += 1
        else:
            enc_msg.append(shift_by_letter(letter, extn_key[key_index]))
            key_index +=1

    return "".join(enc_msg)

def scytale_cipher(message, shift):
    initial_len = len(message)
    if initial_len % shift != 0:
        padding_len = shift - (initial_len % shift)
        message += "_" * padding_len
    padded_len = len(message)
    enc_msg = [""] * padded_len
    for i in range(padded_len):
        enc_index = (i // shift) + (padded_len // shift) * (i % shift)
        enc_msg[i] = message[enc_index]
    return "".join(enc_msg)

def scytale_decipher(message, shift):
    msg_len = len(message)
    dec_msg = [""] * msg_len
    for i in range(msg_len):
        dec_index = (i % shift) * (msg_len // shift) + (i // shift)
        dec_msg[dec_index] = message[i]
    return "".join(dec_msg)