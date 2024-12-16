import sqlite3
import hashlib
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import mpok.dashboard as adminlogin
import user.dashboard as userlogin

conn = sqlite3.connect("db_p3l.db")
cursor = conn.cursor()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_default_admin(username, password):
    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO login (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, "admin"))
    conn.commit()

def login():    
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hash_password(password)
    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty!")
        return

    # Verifikasi role
    cursor.execute("SELECT role FROM login WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()

    if user:
        role = user[0]
        messagebox.showinfo("Login Successful", f"Welcome, {username}! Your role is {role}.")
        # Fitur disini
        app.destroy
        
        if role == "admin":
            adminlogin.main(app)
        elif role == "user":
            userlogin.main(app)
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 4
    window.geometry(f"{width}x{height}+{x}+{y}")

# App Windows GUI
app = ctk.CTk()
center_window(app, 850, 650)
app.resizable(0, 0)
app.title("IndieKost Warehouse")
ctk.set_appearance_mode("Light")  

# Images
side_img_data = Image.open("./Asset/Image/side-img.png")
email_icon_data = Image.open("./Asset/Image/email-icon.png")
password_icon_data = Image.open("./Asset/Image/password-icon.png")

side_img = ctk.CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(550, 650))
email_icon = ctk.CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = ctk.CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

# Layout
ctk.CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = ctk.CTkFrame(master=app, width=300, height=650, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

ctk.CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
ctk.CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

ctk.CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
username_entry = ctk.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
username_entry.pack(anchor="w", padx=(25, 0))

ctk.CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = ctk.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

ctk.CTkButton(master=frame, text="Login", command=login, fg_color="#601E88", text_color="#ffffff").pack(anchor="w", pady=(30, 0), padx=(25, 0))
app.mainloop()

# Add Default Admin
try:
    register_default_admin("mpok", "adminmpok@123")
except sqlite3.IntegrityError:
    pass
