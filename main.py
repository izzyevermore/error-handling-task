from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Authentification")
window.geometry("500x500")
window.config(bg="black")

# Creating header that says 'Please enter login details'

heading = Label(window, text="Please enter login details", font=("Helvetica", 10))
heading.pack()

user = StringVar()
password = StringVar()


# Creating Username label and entry

username = Label(window, text="Username", font=("Helvetica", 10))
username.pack(pady=10)

username_entry = Entry(textvariable=user, width=40)
username_entry.pack(pady=2)

# Creating Password label and entry
password_label = Label(window, text="Password", font=("Helvetica", 10))
password_label.pack(pady=7)

password_entry = Entry(textvariable=password, show="*", width=40)
password_entry.pack(pady=2)

# Creating login button and function

def login():
# Creating a GUI for calculation

    amount = IntVar()

    root = Tk()
    root.title("Exception Handling")
    root.geometry("700x500")
    root.config(bg="black")

# Creating label and entry for calculating

    account_amount = Label(root, text="Please enter amount in account: ", font=("Helvetica", 10))
    account_amount.pack()

    amount_entry = Entry(root, textvariable=amount, width=40)
    amount_entry.pack(pady=5)
    window.withdraw()
# Creating button that is defined with checking if user has enough to go to thailand
    def calculate():
        if int(amount_entry.get()) <= 3000:
            messagebox.showinfo("VALUEerror", "YOU HAVE INSUFFICIENT FUNDS")
            raise ValueError
        else:
            messagebox.showinfo("WELL DONE", "YOU QUALIFY TO GO TO MALAYSIA")


    calculate_btn = Button(root, textvariable=amount, command=calculate, font=("Helvetica", 10), width=30)
    calculate_btn.pack()









login_btn = Button(window, text="Login", command=login, font=("Helvetica", 10), width=30)
login_btn.pack(pady=5)











window.mainloop()
