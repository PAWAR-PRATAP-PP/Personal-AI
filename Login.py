from tkinter import *
from tkinter import messagebox, font
from PIL import ImageTk, Image
from subprocess import call
import mysql.connector
import os
import sys

# ------------------------ Functions ------------------------

def getvals():
    if not username_entry.get():
        messagebox.showinfo("", "Please enter username")
        username_entry.focus_set()
    elif not password_entry.get():
        messagebox.showinfo("", "Please enter password")
        password_entry.focus_set()
    else:
        try:
            mysqldb = mysql.connector.connect(
                host="localhost", user="root", password="Pawar", database="project"
            )
            mycursor = mysqldb.cursor()
            username = username_entry.get()
            password = password_entry.get()

            sql = "SELECT * FROM login WHERE username = %s AND password = %s"
            mycursor.execute(sql, (username, password))
            result = mycursor.fetchone()

            if result:
                messagebox.showinfo("Login", "Login Successful")
                root.destroy()
                call(['python', 'JarvisUi.py'])
            else:
                messagebox.showerror("Login Failed", "Invalid Username or Password")
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                username_entry.focus_set()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
        finally:
            if mysqldb.is_connected():
                mycursor.close()
                mysqldb.close()

def cancel():
    root.destroy()

def register():
    root.destroy()
    call(['python', 'Registration.py'])

def dbaccess():
    root.destroy()
    call(['python', 'dbaccess.py'])

def forgot_pass():
    root.destroy()
    call(['python', 'ForgetPass.py'])

# ------------------------ GUI Layout ------------------------

root = Tk()
root.title('Shravan Login')
root.geometry("700x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Sidebar with image
sidebar = Frame(root, bg="#1a1a2e", width=280)
sidebar.pack(side=LEFT, fill=Y)

# Load and display logo or background image
try:
    img = Image.open("D:\\python\\login.png")
    img = img.resize((260, 260))
    photo = ImageTk.PhotoImage(img)
    label_img = Label(sidebar, image=photo, bg="#1a1a2e")
    label_img.place(x=10, y=70)
except:
    Label(sidebar, text="Shravan", font=("Helvetica", 22), fg="white", bg="#1a1a2e").pack(pady=100)

# Main form area
form_frame = Frame(root, bg="#f0f0f0")
form_frame.pack(expand=True)

Label(form_frame, text="Login Form", font=("Segoe UI", 20, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

# Username
Label(form_frame, text="Username", font=("Segoe UI", 12), bg="#f0f0f0").pack()
username_entry = Entry(form_frame, font=("Segoe UI", 12), width=30, bd=2, relief=GROOVE)
username_entry.pack(pady=5)

# Password
Label(form_frame, text="Password", font=("Segoe UI", 12), bg="#f0f0f0").pack()
password_entry = Entry(form_frame, font=("Segoe UI", 12), show='*', width=30, bd=2, relief=GROOVE)
password_entry.pack(pady=5)

# Buttons
Button(form_frame, text="Login", command=getvals, bg="#1a73e8", fg="white", font=("Segoe UI", 12), width=15).pack(pady=10)
Button(form_frame, text="Cancel", command=cancel, bg="gray", fg="white", font=("Segoe UI", 11), width=10).pack()

# Links
link_frame = Frame(form_frame, bg="#f0f0f0")
link_frame.pack(pady=10)

Button(link_frame, text="Register", command=register, border=0, bg="#f0f0f0", fg="#1a73e8", cursor="hand2").grid(row=0, column=0, padx=5)
Button(link_frame, text="Forgot Password?", command=forgot_pass, border=0, bg="#f0f0f0", fg="#1a73e8", cursor="hand2").grid(row=0, column=1, padx=5)
Button(link_frame, text="Database", command=dbaccess, border=0, bg="#f0f0f0", fg="#1a73e8", cursor="hand2").grid(row=0, column=2, padx=5)

root.mainloop()
