from tkinter import *
from tkinter import messagebox
import sqlite3
def display_trainor_page():
    # Close the current window
    window.destroy()
    import trainor
def display_trainee_page():
    # Close the current window
    window.destroy()
    import trainee    

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == '' or password == '':
        messagebox.showerror("Error", "All fields are required.")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        # Extract the role from the user data
        role = user[4]  # Assuming role is stored in the 5th column (index 4)
        
        messagebox.showinfo("Success", "Login Successful!")

        # Import and run the trainor or trainee page script based on the role
        if role == 'Trainer':
                display_trainor_page()
        elif role == 'Trainee':
            display_trainee_page()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def signup():
    window.destroy()
    import signup


# Create main window
window = Tk()
window.title("Login")
window.geometry('1570x780')
window.configure(bg='#aec8e6')

# Load background image
img = PhotoImage(file='bg2.png')
Label(window, image=img).place(x=180, y=85)

# Get the size of the background image
bg_width = img.width()
bg_height = img.height()

# Create a frame for the login page form
frame = Frame(window, height=bg_height, width=bg_width, bg='white')
frame.place(x=780, y=85)

# Heading for the login form
heading = Label(frame, pady=160, padx=160, text='Login', fg='#00008b', bg='white',
                font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.grid(row=0, columnspan=2)

# Labels and Entry fields
Label(frame, text="Username:").grid(row=1, column=0)
username_entry = Entry(frame)
username_entry.grid(row=1, column=1)

Label(frame, text="Password:").grid(row=2, column=0)
password_entry = Entry(frame, show="*")
password_entry.grid(row=2, column=1)

# Login button
Button(frame, text="Login", command=login).grid(row=3, columnspan=2, pady=10)

# Signup button
Button(frame, text="Sign Up", command=signup).grid(row=4, columnspan=2, pady=10)

window.mainloop()
