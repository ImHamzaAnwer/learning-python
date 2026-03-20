alphabets = [
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

direction = input("type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("type your message: ")
shift = input("Type your shift number: ")


def caesar(direction, original_text, shift_amount):
    ciphered_text = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabets:
            ciphered_text += letter
        else:
            shifted_index = alphabets.index(letter) + shift_amount
            shifted_index %= len(alphabets)
            ciphered_text += alphabets[shifted_index]

    print(f"here is the {direction}d text: {ciphered_text}")


caesar(direction, text, shift)
