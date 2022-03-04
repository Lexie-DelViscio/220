def encode(message, key):
    encode_output = []
    for letter in message:
        encode_output.append(str(ord(letter) + key))
    output = ""
    for letters in encode_output:
        output = output + chr(eval(letters))
    return output


def encode_better(message, key):
    output_string = ""
    for i in range(len(message)):
        character_shift = ord(message[i]) - 65
        shift_value = ord(key[i % len(key)]) - 65
        shift_value_mod = (character_shift + shift_value) % 58
        new_letter = chr(shift_value_mod + 65)
        output_string = output_string + new_letter
    return output_string
