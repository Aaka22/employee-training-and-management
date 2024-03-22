from tkinter import *
from tkinter import messagebox
import sqlite3

# Function to open the login page
def open_homepage():
    # Close the current window
    window.destroy()
    
    # Import and run the login page script
    import homepage

def logout():
    # Open the login page
    open_homepage()

def display_events():
    conn = sqlite3.connect("trainer.db")
    cursor = conn.cursor()
    cursor.execute("SELECT event_name FROM events")
    events = cursor.fetchall()
    conn.close()
    
    event_list = "\n".join([event[0] for event in events])
    messagebox.showinfo("Events", f"Events:\n{event_list}")

def display_materials():
    conn = sqlite3.connect("trainer.db")
    cursor = conn.cursor()
    cursor.execute("SELECT material_name FROM materials")
    materials = cursor.fetchall()
    conn.close()
    
    material_list = "\n".join([material[0] for material in materials])
    messagebox.showinfo("Materials", f"Materials:\n{material_list}")

# Create main window
window = Tk()
window.title("Trainee Application")
window.geometry('600x400')
window.configure(bg='#f0f0f0')

# Load background image
img = PhotoImage(file='OIP.png')
Label(window, image=img, height=600, width=550).place(x=180, y=85)

# Heading for the trainee form
heading = Label(window, text='Welcome Trainee, let\'s see what events you got waiting for you ', fg='red', bg='white',
                font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.place(relx=0.5, rely=0.1, anchor=N)

# See Events button
btn_see_events = Button(window, text="See Events", command=display_events, bg='#4CAF50', fg='white', font=('Arial', 14, 'bold'))
btn_see_events.place(relx=0.5, rely=0.3, anchor=CENTER)

# See Materials button
btn_see_materials = Button(window, text="See Materials", command=display_materials, bg='#f44336', fg='white', font=('Arial', 14, 'bold'))
btn_see_materials.place(relx=0.5, rely=0.7, anchor=CENTER)

# Logout button
btn_logout = Button(window, text="Logout", command=logout, bg='#FFA500', fg='white', font=('Arial', 14, 'bold'))
btn_logout.place(relx=0.9, rely=0, anchor=NE)

window.mainloop()
