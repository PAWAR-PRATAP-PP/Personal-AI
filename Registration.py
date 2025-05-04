from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from subprocess import call
import mysql.connector

# -------------------- Registration Logic --------------------

def getvals():
    username = username_entry.get()
    password = password_entry.get()
    cpassword = confirm_password_entry.get()

    if not username:
        messagebox.showwarning("Input Error", "Please enter a username.")
        username_entry.focus_set()
    elif not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        password_entry.focus_set()
    elif password != cpassword:
        messagebox.showwarning("Mismatch", "Passwords do not match.")
        confirm_password_entry.focus_set()
    else:
        try:
            mysqldb = mysql.connector.connect(
                host="localhost", user="root", password="Pawar", database="project"
            )
            mycursor = mysqldb.cursor()

            sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
            mycursor.execute(sql, (username, password))
            mysqldb.commit()

            messagebox.showinfo("Success", "Registration complete!")
            root.destroy()
            call(['python', 'Login.py'])

            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            confirm_password_entry.delete(0, 'end')

        except mysql.connector.Error as err:
            messagebox.showerror("Error", "Username already exists or connection issue.")
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            confirm_password_entry.delete(0, 'end')
            username_entry.focus_set()
        finally:
            if mysqldb.is_connected():
                mycursor.close()
                mysqldb.close()

# -------------------- Navigation --------------------

def login():
    root.destroy()
    call(['python', 'Login.py'])

def cancel():
    root.destroy()

# -------------------- GUI Layout --------------------

root = Tk()
root.title("Shravan - Register")
root.geometry("500x400")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Optional background image
try:
    img = Image.open("D:\\python\\reg.jpg")
    img = img.resize((500, 400))
    bg = ImageTk.PhotoImage(img)
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass

# Title
Label(root, text="Register New Account", font=("Segoe UI", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

form_frame = Frame(root, bg="#f0f0f0")
form_frame.pack()

# Username
Label(form_frame, text="Username", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=0, column=0, pady=10, padx=10, sticky="e")
username_entry = Entry(form_frame, font=("Segoe UI", 12), width=30)
username_entry.grid(row=0, column=1, pady=10, padx=10)

# Password
Label(form_frame, text="Password", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=1, column=0, pady=10, padx=10, sticky="e")
password_entry = Entry(form_frame, font=("Segoe UI", 12), show="*", width=30)
password_entry.grid(row=1, column=1, pady=10, padx=10)

# Confirm Password
Label(form_frame, text="Confirm Password", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=2, column=0, pady=10, padx=10, sticky="e")
confirm_password_entry = Entry(form_frame, font=("Segoe UI", 12), show="*", width=30)
confirm_password_entry.grid(row=2, column=1, pady=10, padx=10)

# Buttons
Button(root, text="Register", command=getvals, font=("Segoe UI", 12), bg="#1a73e8", fg="white", width=18).pack(pady=10)
Button(root, text="Cancel", command=cancel, font=("Segoe UI", 11), bg="gray", fg="white", width=10).pack()

Button(root, text="Already have an account? Sign in", command=login, font=("Segoe UI", 10, "underline"),
       border=0, bg="#f0f0f0", fg="#1a73e8", cursor="hand2").pack(pady=5)

root.mainloop()
