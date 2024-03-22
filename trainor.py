from tkinter import *
from tkinter import messagebox
import sqlite3

# Function to open the login page
def open_homepage():
    # Close the current window
    window.destroy()
    
    # Import and run the login page script
    import homepage

def add_event():
    event_name = event_entry.get()
    event_date = date_entry.get()

    if event_name == '' or event_date == '':
        messagebox.showerror("Error", "All fields are required.")
        return

    conn = sqlite3.connect("trainer.db")
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, event_name TEXT, event_date TEXT)")
        cursor.execute("INSERT INTO events (event_name, event_date) VALUES (?, ?)", (event_name, event_date))
        conn.commit()
        messagebox.showinfo("Success", "Event added successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to add event: {e}")
    finally:
        conn.close()
        event_entry.delete(0, END)
        date_entry.delete(0, END)

def add_material():
    material_name = material_entry.get()

    if material_name == '':
        messagebox.showerror("Error", "Material name is required.")
        return

    conn = sqlite3.connect("trainer.db")
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS materials (id INTEGER PRIMARY KEY, material_name TEXT)")
        cursor.execute("INSERT INTO materials (material_name) VALUES (?)", (material_name,))
        conn.commit()
        messagebox.showinfo("Success", "Material added successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to add material: {e}")
    finally:
        conn.close()
        material_entry.delete(0, END)

def logout():
    # Open the login page
    open_homepage()

# Create main window
window = Tk()
window.title("Trainer Application")
window.geometry('600x400')
window.configure(bg='#f0f0f0')

# Load background image
img = PhotoImage(file='bg2.png')
Label(window, image=img, height=600, width=550).place(x=180, y=85)

# Heading for the trainer form
heading = Label(window, text='Welcome Trainer', fg='red', bg='white',
                font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.place(relx=0.5, rely=0.1, anchor=N)

# Add Events section
event_label = Label(window, text="Event Name:", bg='white')
event_label.place(relx=0.6, rely=0.3, anchor=E)
event_entry = Entry(window)
event_entry.place(relx=0.7, rely=0.3, anchor=W)

date_label = Label(window, text="Event Date:", bg='white')
date_label.place(relx=0.6, rely=0.4, anchor=E)
date_entry = Entry(window)
date_entry.place(relx=0.7, rely=0.4, anchor=W)

btn_add_event = Button(window, text="Add Event", command=add_event, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
btn_add_event.place(relx=0.8, rely=0.5, anchor=CENTER)

# Add Materials section
material_label = Label(window, text="Material Name:", bg='white')
material_label.place(relx=0.6, rely=0.6, anchor=E)
material_entry = Entry(window)
material_entry.place(relx=0.7, rely=0.6, anchor=W)

btn_add_material = Button(window, text="Add Material", command=add_material, bg='#f44336', fg='white', font=('Arial', 12, 'bold'))
btn_add_material.place(relx=0.8, rely=0.7, anchor=CENTER)

# Logout button
btn_logout = Button(window, text="Logout", command=logout, bg='#FFA500', fg='white', font=('Arial', 12, 'bold'))
btn_logout.place(relx=0.9, rely=0, anchor=NE)

window.mainloop()
