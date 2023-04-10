from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Password Generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # password_list = []

    password_letter = [choice(letters) for i in range(randint(8, 10))]
    password_symbol = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# Save password
def save_password():
    website = website_input.get()
    email = email_input.get()
    password_data = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password_data,
        }
    }
    if len(website) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        # with open("data.json", mode="w") as data_file:
        #     json.dump(new_data, data_file,indent=4)
        try:
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                # create json file and add new data
                json.dump(new_data, data_file, indent=4)
        else:
            # update old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

# Search for password and email
def search_credentials():
    website_name = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website_name} exists.")


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
website_input = Entry(width=32)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = Entry(width=51)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "anu@gmail.com")
password_input = Entry(width=32)
password_input.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command=search_credentials)
search_button.grid(row=1, column=2)

window.mainloop()
