import random


words = [
    "camel",
    "shoes",
    "wardrobe",
    "telephone",
    "clarity",
    "functionality",
    "delete",
]

chosen_word = random.choice(words)
placeholder = ""
lives = 6


for letter in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("\n\nGuess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("~~~~~~~~~~~~ YOU WIN ~~~~~~~~~~~~")

    if guess not in display:
        lives -= 1
        print(f"\n============= {lives} out of 6 lives left =============")
        if lives == 0:
            game_over = True
            print(
                f'============= You Lose, the correct word is "{chosen_word}" ============='
            )
