from tkinter import *
from tkinter import messagebox
from password_generator import create_password
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

hero_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=hero_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_input = Entry()
website_input.grid(row=1, column=1)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_input = Entry()
email_input.insert(0, "ash@gmail.com")
email_input.grid(row=2, column=1)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.grid(row=3, column=1)


def gen_password():
    new_password = create_password()
    password_input.insert(0, new_password)


def confirm():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    pyperclip.copy(f"{password}")
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        res = messagebox.askquestion(f"{website}", f"Email:{email}\nPassword:{password}\nIs this ok?")
        if res == "yes":
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)
        else:
            messagebox.showinfo("Return", "Returning to main application")


def find_password():
    with open("data.json") as file:
        data = json.load(file)
    website = website_input.get()
    try:
        messagebox.showinfo(f"{website}", f"Email:{data[website]['email']}\nPassword:{data[website]['password']}")
    except KeyError:
        messagebox.showinfo("Error", "No Data File Found.")


search_btn = Button(text="Search", command=find_password, width=15)
search_btn.grid(row=1, column=2)

gen_btn = Button(text="Generate Password", command=gen_password, width=15)
gen_btn.grid(row=3, column=2)

confirm_btn = Button(text="Add", command=confirm)
confirm_btn.grid(row=4, column=1)

window.mainloop()
