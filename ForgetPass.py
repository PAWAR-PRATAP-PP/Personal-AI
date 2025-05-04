from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

# ------------------- Reset Password Function -------------------

def fetch_data():
    username = username_entry.get()
    password = password_entry.get()
    cpassword = cpassword_entry.get()

    if not username or not password or not cpassword:
        messagebox.showwarning("Missing Fields", "All fields are required")
        return

    if password != cpassword:
        messagebox.showerror("Mismatch", "Passwords do not match")
        return

    try:
        mysqldb = mysql.connector.connect(
            host="localhost", user="root", password="Pawar", database="project"
        )
        mycursor = mysqldb.cursor()

        # Check if username exists
        sql = "SELECT username FROM login WHERE username=%s"
        mycursor.execute(sql, (username,))
        result = mycursor.fetchone()

        if result is None:
            messagebox.showerror("Not Found", "Username does not exist")
        else:
            update_qry = "UPDATE login SET password=%s WHERE username=%s"
            mycursor.execute(update_qry, (password, username))
            mysqldb.commit()
            messagebox.showinfo("Success", "Password Reset Successfully")
            

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        if mysqldb.is_connected():
            mycursor.close()
            mysqldb.close()

# ---------------------- GUI Layout ----------------------

root = Tk()
root.title("Shravan - Reset Password")
root.geometry("500x400")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Optional Background Image (skip if not found)
try:
    bg_img = Image.open("D:\\python\\login.png")
    bg_img = bg_img.resize((500, 400))
    bg_photo = ImageTk.PhotoImage(bg_img)
    Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass

# Heading
Label(root, text="Reset Your Password", font=("Segoe UI", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

form_frame = Frame(root, bg="#f0f0f0")
form_frame.pack()

# Username
Label(form_frame, text="Username", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=0, column=0, pady=10, padx=10, sticky="e")
username_entry = Entry(form_frame, font=("Segoe UI", 12), width=25)
username_entry.grid(row=0, column=1, pady=10, padx=10)

# New Password
Label(form_frame, text="New Password", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=1, column=0, pady=10, padx=10, sticky="e")
password_entry = Entry(form_frame, font=("Segoe UI", 12), show="*", width=25)
password_entry.grid(row=1, column=1, pady=10, padx=10)

# Confirm Password
Label(form_frame, text="Confirm Password", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=2, column=0, pady=10, padx=10, sticky="e")
cpassword_entry = Entry(form_frame, font=("Segoe UI", 12), show="*", width=25)
cpassword_entry.grid(row=2, column=1, pady=10, padx=10)

# Submit Button
Button(root, text="Reset Password", command=fetch_data, font=("Segoe UI", 12),
       bg="#1a73e8", fg="white", width=20).pack(pady=20)

root.mainloop()
