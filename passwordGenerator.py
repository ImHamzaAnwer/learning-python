import random

letters = [
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

numOfAlphabets = int(input("How many alphabets do you want to include ? "))
numOfNumbers = int(input("How many numbers do you want to include ? "))
numOfChars = int(input("How many characters do you want to include ? "))
passwordArray = []

for alphabet in range(0, numOfAlphabets):
    passwordArray.append(random.choice(letters))

for number in range(0, numOfNumbers):
    passwordArray.append(random.choice(numbers))

for char in range(0, numOfChars):
    passwordArray.append(random.choice(symbols))


random.shuffle(passwordArray)
password = ""
for char in passwordArray:
    password += char

print(f"your password is {password}")
