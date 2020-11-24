alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position >= len(alphabet):
            rewind_position = new_position - len(alphabet)
            cipher_text += alphabet[rewind_position]
        else:
            cipher_text += alphabet[new_position]

    print(f"The encoded text is {cipher_text}")


def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        decrypted_text += alphabet[new_position]

    print(f"The decoded text is {decrypted_text}")


if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text=text, shift=shift)
