from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


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


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(5, 8))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        return messagebox.showwarning(message="Do not leave any field empty")

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"Email {email}\n Password: {password}\n Are you sure you want to save this data?",
    )

    if is_ok:
        with open("password_manager/passwords.txt", "a") as f:
            f.write(f"{website} | {email} | {password}\n")

        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)
        messagebox.showinfo(message="Your password has been saved !")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas()
canvas.config(width=200, height=200)
lock_image = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")

website_label.grid(column=0, row=1)
website_input = Entry(
    width=35,
)
website_input.focus()
website_input.grid(column=1, columnspan=2, row=1)


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, columnspan=2, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(width=10, text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)


add_button = Button(text="Add", width=33, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
