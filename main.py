from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white")
canvas.grid(column=1, row=0)

#website label part
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_label.config(padx=0, pady=5)


website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

#email label part
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_label.config(padx=0, pady=5)
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)

#password label part
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_label.config(padx=0, pady=5)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(width=43, text="Add")
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
