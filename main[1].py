import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_char = [random.choice(letters) for x in range(random.randint(8, 10))]
    numbers_char = [random.choice(numbers) for x in range(random.randint(2, 4))]
    symbols_char = [random.choice(symbols) for x in range(random.randint(2, 4))]
    password_list = letters_char + numbers_char + symbols_char

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def button_clicked():
    new_text = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()}}
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Warning", message="Do not leave any field empty")
    else:
        try:
            with open("pw_manager.json", "r") as text_file:
                data = json.load(text_file)
        except FileNotFoundError:
            with open("pw_manager.json", "w") as text_file:
                json.dump(new_text, text_file, indent=4)
        else:
            data.update(new_text)
            with open("pw_manager.json", "w") as text_file:
                json.dump(data, text_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white")
canvas.grid(column=1, row=0)

# website label part
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_label.config(padx=0, pady=5)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# email label part
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_label.config(padx=0, pady=5)
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "rachel12eve@hotmail.com")

# password label part
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_label.config(padx=0, pady=5)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=pw_generator)
generate_button.grid(column=2, row=3)

add_button = Button(width=43, text="Add", command=button_clicked)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
