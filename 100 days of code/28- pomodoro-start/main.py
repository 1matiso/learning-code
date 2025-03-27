from itertools import count
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count(long_break_sec)
        reps = 0
        timer_label.config(text="Long Break", fg = GREEN)
        mark = ""
        if reps % 2 == 0:
           mark += "✔"
        check_label.config(text = mark)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break", fg = PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg = RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=YELLOW)

timer_label = Label(font=("courier", 40, "bold"), text="", fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(text = "", fg=GREEN,bg=YELLOW, font=("courier", 15))
check_label.grid(column=1, row=3)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 132, text="0:00", fill="white", font=(FONT, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)





window.mainloop()
