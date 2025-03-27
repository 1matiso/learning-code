from tkinter import *
from tkinter import messagebox
import random
import json


def save():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()
    new_data = {website: {
        "email": username,
        "password": password,
    }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Error", message="Unable to add data, one of the inputs is empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}

            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

            password_entry.delete(0, END)
            username_entry.delete(0, END)
            website_entry.delete(0, END)
            website_entry.focus()


def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)



    password_entry.insert(0, password)

def search():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data:
                messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="Website not in database")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, sticky="e")
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, sticky="w")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", command=pw_generator)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

search_button = Button(text="Search", width=13, command= search)
search_button.grid(row=1, column=2)

window.grid_rowconfigure(4, weight=1)

window.mainloop()
