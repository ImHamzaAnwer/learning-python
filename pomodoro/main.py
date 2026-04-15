import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.3
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 1

reps = 0
timer = None
checkmark_icon = ""


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    main_title.config(text="Pomodoro")
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_secs = math.floor(WORK_MIN * 60)
    short_break_secs = math.floor(SHORT_BREAK_MIN * 60)
    long_break_secs = math.floor(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        main_title.config(text="Long Break", fg=RED)
        count_down(long_break_secs)
    elif reps % 2 == 0:
        main_title.config(text="Break", fg=PINK)
        count_down(short_break_secs)
    else:
        main_title.config(text="Work", fg=GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark_icon = ""
        number_of_sessions = math.floor(reps / 2)
        for _ in range(number_of_sessions):
            checkmark_icon += "✔"
        checkmark.config(text=checkmark_icon)


# ---------------------------- UI SETUP ------------------------------- #

import tkinter

window = tkinter.Tk()
window.config(padx=80, pady=50, bg=YELLOW)
window.title("Pomodoro")

main_title = tkinter.Label(
    text="Pomodoro",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 28, "normal"),
)
main_title.grid(row=0, column=1)

tomtato_img = tkinter.PhotoImage(file="pomodoro/tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomtato_img)

timer_text = canvas.create_text(
    100, 134, text="00:00", fill="white", font=(FONT_NAME, 20, "bold")
)
canvas.grid(row=1, column=1)


start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


checkmark = tkinter.Label(
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 25, "normal"),
)
checkmark.grid(row=3, column=1)

window.mainloop()
