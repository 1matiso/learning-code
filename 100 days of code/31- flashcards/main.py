from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"

df = read_csv("flashcards de-en.csv")
words = DataFrame.to_dict(df, orient="records")
current_card = random.choice(words)

correct_guesses = []

def game_reset():
    global current_card
    guess.delete(0, END)
    canvas.itemconfig(correct_text, state="hidden")
    canvas.itemconfig(wrong_text, state="hidden")
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(card_title, text="German")
    current_card = random.choice(words)
    canvas.itemconfig(card_word, text=f"{current_card['German']}")


def check_guess():
    user_guess = guess.get()
    if len(user_guess) < 1:
        pass
    elif user_guess == current_card["English"]:
        canvas.itemconfig(correct_text, state="normal")
        canvas.itemconfig(card, image=card_back)
        canvas.itemconfig(card_title, text= "English")
        canvas.itemconfig(card_word, text=f"{current_card['English']}")

        window.after(3000, game_reset)

    else:
        canvas.itemconfig(wrong_text, state="normal")
        canvas.itemconfig(card, image=card_back)
        canvas.itemconfig(card_title, text= "English")
        canvas.itemconfig(card_word, text=f"{current_card['English']}")
        window.after(3000, game_reset)





window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
check_image = PhotoImage(file="right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font="Helvetica 30 italic", text="German", fill="black")
card_word = canvas.create_text(400, 263, font="Helvetica 60 bold", text=f"{current_card['German']}", fill="black")
correct_text = canvas.create_text(400, 400, font="Helvetica 30 bold", text="Correct!", fill="green", state="hidden")
wrong_text = canvas.create_text(400, 400, font="Helvetica 30 bold", text="Wrong!", fill="red", state="hidden")
canvas.grid(row=0, column=0)

check_button = Button(bg=BACKGROUND_COLOR, fg= BACKGROUND_COLOR,command=check_guess)
check_button.place(x=1000,y=1000)
window.bind('<Return>', lambda event: check_button.invoke())

guess = Entry(width=30, font="helvetica 30 bold", justify="center")
guess.grid(row=2, column=0)



guess.focus()










window.mainloop()
