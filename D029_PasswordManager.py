'''
INFORMATION:
    • This program lets us save passwords to a file in the user computer.
    • These passwords can be manually typed OR we can auto generate them.
    • We need 'pyperclip' module of Python to copy the password to the clipboard.
      So we need to run the following command in the terminal - 
      "pip install pyperclip"
    • The 'tkinter' module is used to make the Password Manager.
      [ 'tkinter' Documentations Link ]
        Link:- https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
        Link:- https://docs.python.org/3/library/tk.html

'''

# Code For The Password Manager
import pyperclip, random, json
from tkinter import *
from tkinter import messagebox


# CREATING THE WINDOW:-  --------------------------------------------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)


# CREATING A CANVAS TO HOLD IMAGE:-  --------------------------------------------------------------
canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="Database/_PasswordLogo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(row=0, column=1)


# CREATING ALL THE LABELS:-  ----------------------------------------------------------------------
# Creating the labels
label_website = Label(text="Website:")
label_email = Label(text="Email/Username:")
label_pass = Label(text="Password:")
# Putting the labels on the window
label_website.grid(row=1, column=0)
label_email.grid(row=2, column=0)
label_pass.grid(row=3, column=0)


# CREATING ALL ENTRY FIELDS OR INPUT FIELDS:-  ----------------------------------------------------
# Creating the entry fields
enter_website = Entry(width=20)
enter_website.focus()
enter_email = Entry(width=36)
enter_email.insert(0, "youremail@gmail.com")
enter_pass = Entry(width=20)
# Putting the entry fields on the screen
enter_website.grid(row=1, column=1)
enter_email.grid(row=2, column=1, columnspan=2)
enter_pass.grid(row=3, column=1)


# FUNCTION TO ADD PASSWORDS:-  --------------------------------------------------------------------
def addPassword():
    # Getting data from each input field
    website = enter_website.get()
    email = enter_email.get()
    password = enter_pass.get()

    # Format of new data to be added
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Checking if any input field is blank or not
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message=f"Seems like you left some fields empty.")
    else:
        try:
            with open(file="Database/File_PasswordsData.json", mode="r") as data_file:
                # Loading json data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="Database/File_PasswordsData.json", mode="w") as data_file:
                # Saving json data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating json data
            data.update(new_data)
            with open(file="Database/File_PasswordsData.json", mode="w") as data_file:
                # Saving the updated json data
                json.dump(data, data_file, indent=4)
        finally:
            # Clearing previous data from the input(entry) fields
            enter_website.delete(0, END)
            enter_pass.delete(0, END)
            enter_website.focus()


# FUNCTION TO GENERATE RANDOM PASSWORDS:-  --------------------------------------------------------
def generatePassword():
    total_letters = random.randint(2, 6)
    total_numbers = random.randint(2, 4)
    total_symbols = random.randint(2, 3)

    # List of all characters to be used in password
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%&()"

    password_list = [random.choice(letters) for _ in range(total_letters)]
    password_list.extend([random.choice(numbers) for _ in range(total_numbers)])
    password_list.extend([random.choice(symbols) for _ in range(total_symbols)])

    random.shuffle(password_list)
    generated_password = ''.join(password_list)
    pyperclip.copy(generated_password)

    enter_pass.delete(0, END)
    enter_pass.insert(0, generated_password)


# FUNCTION TO SEARCH OR FIND A PASSWORD:-  --------------------------------------------------------
def findPassword():
    website = enter_website.get()

    # Checking if website field is empty
    if len(website) == 0:
        messagebox.showinfo(
            title="Website ?", message="Please provide the wesite name you want to search.")
    else:
        # Checking if passwords file exists or not
        try:
            with open(file="Database/File_PasswordsData.json", mode="r") as data_file:
                # Loading json data
                data = json.load(data_file)
        except FileNotFoundError:
            # Showing error message
            messagebox.showerror(title="Error", message="No data file found.")
        else:
            # Fetching the required data
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(
                    title=website, message=f"Email:- {email}\nPassword:- {password}")
            else:
                messagebox.showinfo(
                    title=website, message=f"There is no data for '{website}'.")


# CREATING ALL BUTTONS:-  -------------------------------------------------------------------------
# Creating the buttons
btn_search_pass = Button(text="Search", width=16, command=findPassword)
btn_generate_pass = Button(text="Generate Password", command=generatePassword)
btn_add_pass = Button(text="Add", width=36, command=addPassword)
# Putting the buttons on the screen
btn_search_pass.grid(row=1, column=2)
btn_generate_pass.grid(row=3, column=2)
btn_add_pass.grid(row=4, column=1, columnspan=2)



# THIS LINE KEEPS THE WINDOW ACTIVE:-  ------------------------------------------------------------
window.mainloop()
