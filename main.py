from tkinter import *
from tkinter import messagebox

# Save password
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                  f"Password: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)
                website_input.focus()




# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=51)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=51)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "anu@gmail.com")
password_input = Entry(width=32)
password_input.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
