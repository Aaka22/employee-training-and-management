from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
# Function to open the login page
def open_login():
    # Close the current window
    window.destroy()
    
    # Import and run the login script
    import login


# Function to register a user
def register():
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    role = role_var.get()

    if email == '' or username == '' or password == '' or confirm_password == '' or role == '':
        messagebox.showerror("Error", "All fields are required.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, username TEXT, password TEXT, role TEXT)")
        cursor.execute("INSERT INTO users (email, username, password, role) VALUES (?, ?, ?, ?)", (email, username, password, role))
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")
        open_login()  # Open the login after successful registration
    except sqlite3.Error as e:
        messagebox.showerror("Error", "Registration Failed: " + str(e))
    finally:
        conn.close()

    # Clear entry fields after registration
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)
    role_var.set("")

def view_data():
    def delete_user(event):
        selected_item = tree.selection()[0]
        user_id = tree.item(selected_item, "text")
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
            conn.commit()
            messagebox.showinfo("Success", "User deleted successfully.")
            tree.delete(selected_item)
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Failed to delete user: " + str(e))
        finally:
            conn.close()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("No Data", "No data available.")
            return

        top = Toplevel()
        top.title("View Data")

        tree = ttk.Treeview(top)
        tree["columns"] = ("Email", "Username", "Role", "Action")
        tree.heading("#0", text="ID")
        tree.heading("Email", text="Email")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")
        tree.heading("Action", text="Action")

        for row in rows:
            tree.insert("", "end", text=row[0], values=(row[1], row[2], row[4], "Delete"), tags=("tag1",))

        tree.bind("<ButtonRelease-1>", delete_user)

        tree.pack(expand=True, fill="both")
    except sqlite3.Error as e:
        messagebox.showerror("Error", "Failed to fetch data: " + str(e))
    finally:
        conn.close()


# Create main window
window = Tk()
window.title("Sign Up")
window.geometry('1570x780')
window.configure(bg='#aec8e6')

# Load background image
img = PhotoImage(file='bg1.png')
Label(window, image=img, height=600, width=550).place(x=180, y=85)

# Create a frame for the sign-up form
frame = Frame(window, height=600, width=550, bg='white')
frame.place(x=780, y=85)

# Heading for the sign-up form
heading = Label(frame, pady=160, padx=160, text='Sign up', fg='#00008b', bg='white',
                font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.grid(row=0, columnspan=2)

# Labels and Entry fields
Label(frame, text="Email:").grid(row=1, column=0, sticky=E)
email_entry = Entry(frame, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Username:").grid(row=2, column=0, sticky=E)
username_entry = Entry(frame, width=30)
username_entry.grid(row=2, column=1, padx=5, pady=5)

Label(frame, text="Password:").grid(row=3, column=0, sticky=E)
password_entry = Entry(frame, show="*", width=30)
password_entry.grid(row=3, column=1, padx=5, pady=5)

Label(frame, text="Confirm Password:").grid(row=4, column=0, sticky=E)
confirm_password_entry = Entry(frame, show="*", width=30)
confirm_password_entry.grid(row=4, column=1, padx=5, pady=5)

Label(frame, text="Role:").grid(row=5, column=0, sticky=E)
role_var = StringVar()
Radiobutton(frame, text="Trainer", variable=role_var, value="Trainer").grid(row=5, column=1, sticky=W)
Radiobutton(frame, text="Trainee", variable=role_var, value="Trainee").grid(row=5, column=1, sticky=E)

# Register button
Button(frame, text="Register", command=register).grid(row=6, columnspan=2, pady=10)
 
 # View data button
Button(frame, text="View Data", command=view_data).grid(row=7, columnspan=2, pady=10)

window.mainloop()
