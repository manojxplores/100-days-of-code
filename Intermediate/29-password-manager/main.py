from tkinter import *
from tkinter import messagebox
from password_generator import create_password


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

hero_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=hero_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_var = StringVar()
website_input = Entry(textvariable=website_var)
website_input.grid(row=1, column=1)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_var = StringVar()
email_input = Entry(textvariable=email_var)
email_input.grid(row=2, column=1)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

passw_var = StringVar()
password_input = Entry(textvariable=passw_var)
password_input.grid(row=3, column=1)


def gen_password():
    new_password = create_password()
    passw_var.set(new_password)


def confirm():
    website = website_var.get()
    email = email_var.get()
    password = passw_var.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        res = messagebox.askquestion(f"{website}", f"Email:{email}\nPassword:{password}\nIs this ok?")
        if res == "yes":
            with open("data.txt", mode='a') as file:
                file.write(f"{website} | {email} | {password}\n")
        else:
            messagebox.showinfo("Return", "Returning to main application")


gen_btn = Button(text="Generate Password", command=gen_password)
gen_btn.grid(row=3, column=2)

confirm_btn = Button(text="Add", command=confirm)
confirm_btn.grid(row=4, column=1)


# Use pyperclip to copy the text to clipboard
window.mainloop()
