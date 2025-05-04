import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import ImageTk,Image
from colorama import Fore, Back, Style
from subprocess import call

def fetch_data():
    try:
        # Replace 'your_username', 'your_password', 'your_database', and 'your_table' with your MySQL credentials and table information
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Pawar',
            database='project'
        )

        cursor = connection.cursor()

        # database Quary
        query = "SELECT * FROM login"
        cursor.execute(query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the data in the treeview widget
        for row in rows:
            tree.insert('', 'end', values=row)

    except mysql.connector.Error as e:
        print("Error: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def back():
        window.destroy()
        call(['python','Login.py'])

# Create the main window
window = tk.Tk()
window.title("Poject Database")


# Create a treeview widget to display data
columns = ('Username', 'Password')  # Replace with your actual column names
tree = ttk.Treeview(window, columns=columns, show='headings')

# Set column headings
for col in columns:
    tree.heading(col, text=col)

# Pack the treeview widget
tree.pack(pady=10)

# Create a button to fetch data
fetch_button = tk.Button(window, text="Fetch Data", command=fetch_data)
fetch_button.pack()
fetch_button = tk.Button(window, text="Back", command=back)
fetch_button.pack()


# Run the Tkinter event loop
window.mainloop()
