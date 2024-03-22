from tkinter import *

# Function to open the trainor page
def open_login():
    # Close the current window
    window.destroy()
    
    # Import and run the trainor page script
    import login

# Function to open the sign up page
def open_signup():
    # Close the current window
    window.destroy()
    
    # Import and run the signup page script
    import signup
# Create main window
window = Tk()
window.title("Employment Training and Materials")
window.geometry('600x400')
window.configure(bg='#f0f0f0')

# Load background image
img = PhotoImage(file='bg4 (1).png')
Label(window, image=img).place(relx=0.5, rely=0.5, anchor=CENTER)

# Heading for the homepage form
heading = Label(window, text='Welcome To employee training and material ', fg='red', bg='white',
                font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.place(relx=0.5, rely=0.1, anchor=N)

# Add login button
btn_login = Button(window, text=" PRESS HERE TO LOGIN", command=open_login, bg='#FFA500', fg='white', font=('Arial', 14, 'bold'))
btn_login.place(relx=0.5, rely=0.8, anchor=CENTER)

# Add signup button
btn_signup = Button(window, text="PRESS HERE TO SIGN UP", command=open_signup, bg='#FFA500', fg='white', font=('Arial', 14, 'bold'))
btn_signup.place(relx=0.5, rely=0.9, anchor=CENTER)

window.mainloop()
