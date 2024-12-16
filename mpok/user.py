import sqlite3
import hashlib
import customtkinter as ctk
from tkinter import ttk , messagebox
import mpok.dashboard as adminlogin
import mpok.order as adminorder
import mpok.stok as adminstok
import mpok.transaksi as admintransaksi


# Database connection
conn = sqlite3.connect("db_p3l.db")
cursor = conn.cursor()

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Add user function
def add_user(username, password, role):
    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO login (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, role))
    conn.commit()
    print(f"User '{username}' with role '{role}' added successfully!")  # Debug log

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 4
    window.geometry(f"{width}x{height}+{x}+{y}")

# Create popup
def create_popup():
    # Membuat jendela pop-up utama
    popup = ctk.CTk()
    center_window(popup, 600, 250)
    popup.title("Tambah User")
    popup.resizable(False, False)

    # Bagian atas pop-up
    top_frame = ctk.CTkFrame(popup, height=50, corner_radius=0)
    top_frame.pack(side="top", fill="x")

    title_label = ctk.CTkLabel(top_frame, text="Tambah User", font=("Arial", 16, "bold"))
    title_label.pack(side="left", padx=20, pady=10)

    close_button = ctk.CTkButton(
        top_frame,
        text="✖",
        width=30,
        height=30,
        fg_color="red",
        hover_color="darkred",
        command=popup.destroy
    )
    close_button.pack(side="right", padx=10, pady=10)

    # Konten pop-up
    content_frame = ctk.CTkFrame(popup, corner_radius=10)
    content_frame.pack(side="top", fill="both", expand=True, padx=20, pady=10)

    # Username
    user_label = ctk.CTkLabel(content_frame, text="Username:", anchor="w")
    user_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    user_entry = ctk.CTkEntry(content_frame, placeholder_text="Username")
    user_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Password
    password_label = ctk.CTkLabel(content_frame, text="Password:", anchor="w")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = ctk.CTkEntry(content_frame, placeholder_text="Password", show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Role dropdown
    options = ["admin", "user"]
    role_label = ctk.CTkLabel(content_frame, text="Role:", anchor="w")
    role_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    role_dropdown = ctk.CTkOptionMenu(content_frame, values=options)
    role_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Mengatur kolom agar dapat di-resize
    content_frame.grid_columnconfigure(1, weight=1)

    # Tombol OK
    ok_button = ctk.CTkButton(
        popup,
        text="OK",
        fg_color="green",
        hover_color="darkgreen",
        corner_radius=10,
        command=lambda: handle_add_user(popup, user_entry.get(), password_entry.get(), role_dropdown.get()),
    )
    ok_button.pack(side="bottom", pady=10)

    # Menjalankan pop-up
    popup.mainloop()

# Handle add user
def handle_add_user(popup, username, password, role):
    if not username or not password:
        print("Error: Username and password cannot be empty!")  # Debug log
        return
    add_user(username, password, role)
    messagebox.showinfo("Success", f"User '{username}' with role '{role}' added successfully!")
    popup.destroy()

# Setup utama
def setup_app(app):
    # Clear previous widgets
    for widget in app.winfo_children():
        widget.destroy()

    app.title("Indiekost Admin Panel")

    setup_sidebar(app)
    main_frame = setup_main_content(app)

    setup_top_bar(main_frame)

    # Tidak perlu menyebutkan path penuh untuk database
    setup_user_table(main_frame)

    setup_floating_button(main_frame)

    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.mainloop()

# Frame kiri (Menu Navigasi)
def setup_sidebar(root):
    sidebar_frame = ctk.CTkFrame(root, width=200, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, sticky="ns")
    sidebar_frame.grid_propagate(False)

    menu_label = ctk.CTkLabel(sidebar_frame, text="MENU", font=("Arial", 16, "bold"))
    menu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    menu_items = [("Dashboard", lambda: adminlogin.main(root), None),
                  ("Pesanan", lambda: adminorder.lihat_order(root), None),
                  ("Stok Barang", lambda: adminstok.main_ui(root), None),
                  ("Transaksi", lambda: admintransaksi.main(root), None),
                  ("Users", None, "green")
                  ]
    
    for i, (item, action, btn_color) in enumerate(menu_items, start=1):
        button = ctk.CTkButton(sidebar_frame, text=item, command=action or (lambda: None), fg_color=btn_color or None)
        button.grid(row=i, column=0, padx=20, pady=10, sticky="w")

    logout_button = ctk.CTkButton(sidebar_frame, text="Keluar", fg_color="red", hover_color="darkred", command=root.destroy)
    logout_button.grid(row=len(menu_items) + 1, column=0, padx=20, pady=50, sticky="w")

# Frame konten utama
def setup_main_content(root):
    main_frame = ctk.CTkFrame(root, corner_radius=10)
    main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=1)

    user_label = ctk.CTkLabel(main_frame, text="User", font=("Arial", 20, "bold"))
    user_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")
    return main_frame

# Bar atas (Pencarian dan filter)
def setup_top_bar(main_frame):
    top_bar = ctk.CTkFrame(main_frame, corner_radius=0, height=50)
    top_bar.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

    search_entry = ctk.CTkEntry(top_bar, placeholder_text="Search")
    search_entry.pack(side="left", padx=10, pady=10)

    filter_button = ctk.CTkButton(top_bar, text="Filter", fg_color="red", width=70, hover_color="darkred")
    filter_button.pack(side="left", padx=10, pady=10)

# Tabel data pengguna
def setup_user_table(main_frame, db_file="db_p3l.db", table_name="login"):
    table_frame = ctk.CTkFrame(main_frame, corner_radius=10)
    table_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

    tree = ttk.Treeview(table_frame, columns=("Username", "Role"), show="headings")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("Username", text="Username")
    tree.heading("Role", text="Role")

    tree.column("Username", width=200, anchor="w")
    tree.column("Role", width=100, anchor="center")

    def load_data():
        # Hapus data lama dari TreeView
        tree.delete(*tree.get_children())
        try:
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute(f"SELECT username, role FROM {table_name}")
            data = cursor.fetchall()
            for idx, (name, role) in enumerate(data, start=1):
                tree.insert("", "end", values=(name, role))
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error loading data: {e}")
        finally:
            conn.close()

    def delete_user():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Tidak ada data yang di pilih", "Pilih user yang ingin di hapus.")
            return

        username = tree.item(selected_item, "values")[0]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete user '{username}'?")
        if confirm:
            try:
                conn = sqlite3.connect(db_file)
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM {table_name} WHERE username = ?", (username,))
                conn.commit()
                tree.delete(selected_item)
                messagebox.showinfo("Success", f"User '{username}' has been deleted.")
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error deleting user: {e}")
            finally:
                conn.close()

    def edit_user():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Tidak ada data yang di pilih", "Pilih user yang ingin di edit.")
            return

        username, current_role = tree.item(selected_item, "values")

        edit_window = ctk.CTkToplevel(main_frame)
        edit_window.title(f"Edit User - {username}")
        center_window(edit_window, 400, 300)

        ctk.CTkLabel(edit_window, text="New Password").pack(pady=5)
        password_entry = ctk.CTkEntry(edit_window, show="*")
        password_entry.pack(pady=5)

        # Dropdown untuk Role
        options = ["admin", "user"]
        ctk.CTkLabel(edit_window, text="New Role").pack(pady=5)
        role_dropdown = ctk.CTkOptionMenu(edit_window, values=options, width=200)
        role_dropdown.set(current_role)  # Set nilai awal ke role saat ini
        role_dropdown.pack(pady=5)

        def save_changes():
            new_password = password_entry.get().strip()
            new_role = role_dropdown.get()  # Ambil nilai dari dropdown
            if not new_role:
                messagebox.showwarning("Input Error", "Role cannot be empty.")
                return

            hashed_password = hash_password(new_password) if new_password else None
            try:
                conn = sqlite3.connect(db_file)
                cursor = conn.cursor()
                if hashed_password:
                    cursor.execute(
                        f"UPDATE {table_name} SET password = ?, role = ? WHERE username = ?", 
                        (hashed_password, new_role, username)
                    )
                else:
                    cursor.execute(
                        f"UPDATE {table_name} SET role = ? WHERE username = ?", 
                        (new_role, username)
                    )
                conn.commit()
                load_data()
                messagebox.showinfo("Success", f"User '{username}' has been updated.")
                edit_window.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error updating user: {e}")
            finally:
                conn.close()

        ctk.CTkButton(edit_window, text="Save Changes", command=save_changes).pack(pady=20)
        ctk.CTkButton(edit_window, text="Cancel", command=edit_window.destroy).pack()

    load_data()

    # Tombol untuk edit dan hapus
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.grid(row=2, column=0, pady=10, sticky="ew")

    edit_button = ctk.CTkButton(button_frame, text="Edit User", command=edit_user)
    edit_button.pack(side="left", padx=10)

    delete_button = ctk.CTkButton(button_frame, text="Delete User", fg_color="red", command=delete_user)
    delete_button.pack(side="left", padx=10)

# Tombol tambah data
def setup_floating_button(main_frame):
    add_button = ctk.CTkButton(
        main_frame,
        text="+",
        width=50,
        height=50,
        corner_radius=25,
        fg_color="red",
        font=("Arial", 24, "bold"),
        hover_color="darkred",
        command=lambda: create_popup(),
    )
    add_button.place(relx=0.88, rely=0.8, anchor="center")

if __name__ == "__main__":
    setup_app(ctk.CTk())