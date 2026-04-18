from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
try:
    data = pd.read_csv("flash_card_project/data/words_to_learn.csv")
except FileNotFoundError:
    orignial_data = pd.read_csv("flash_card_project/data/turkish_words.csv")
    cards = orignial_data.to_dict(orient="records")
else:
    cards = data.to_dict(orient="records")


def is_known():
    cards.remove(current_card)
    data = pd.DataFrame(cards)
    data.to_csv("flash_card_project/data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_card_timer

    window.after_cancel(flip_card_timer)

    current_card = random.choice(cards)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(language, text="Turkish", fill="black")
    canvas.itemconfig(word, text=current_card["Turkish"], fill="black")

    flip_card_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card, card_back_image
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


# -------------- UI --------------

window = Tk()
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

flip_card_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(file="flash_card_project/images/card_front.png")
card_back_image = PhotoImage(file="flash_card_project/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(400, 120, text="", font=("Ariel", 36, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file="flash_card_project/images/wrong.png")
wrong_button = Button(
    image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card
)
wrong_button.grid(row=2, column=0)

correct_image = PhotoImage(file="flash_card_project/images/right.png")
correct_button = Button(
    image=correct_image,
    highlightthickness=0,
    borderwidth=0,
    command=is_known,
)
correct_button.grid(row=2, column=1)

next_card()
window.mainloop()
