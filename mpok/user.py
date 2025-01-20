import sqlite3
import hashlib
import customtkinter as ctk
from tkinter import ttk, messagebox
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

# Center window function
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 4
    window.geometry(f"{width}x{height}+{x}+{y}")

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

    title_label = ctk.CTkLabel(top_bar, text="User Panel", font=("Arial", 18))
    title_label.pack(pady=10)

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

    def create_popup():
        # Membuat jendela pop-up utama
        popup = ctk.CTk()
        center_window(popup, 600, 250)
        popup.title("Tambah User")
        popup.resizable(False, False)

        # Bagian atas pop-up
        top_frame = ctk.CTkFrame(popup, height=50, corner_radius=0)
        top_frame.pack(side="top", fill="x")

        title_label = ctk.CTkLabel(top_frame, text="Tambah User", font=("Arial", 16))
        title_label.pack(pady=10)

        # Form untuk menambah user
        form_frame = ctk.CTkFrame(popup)
        form_frame.pack(pady=20)

        ctk.CTkLabel(form_frame, text="Username").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        username_entry = ctk.CTkEntry(form_frame)
        username_entry.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Password").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        password_entry = ctk.CTkEntry(form_frame, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Role").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        role_entry = ctk.CTkOptionMenu(form_frame, values=["admin", "user"])  # Dropdown untuk role
        role_entry.grid(row=2, column=1, padx=10, pady=5)

        def submit_new_user():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            role = role_entry.get().strip()  # Mengambil nilai dari dropdown
            if username and password and role:
                add_user(username, password, role)
                load_data()  # Refresh data
                popup.destroy()
                messagebox.showinfo("Success", f"User '{username}' added successfully.")
            else:
                messagebox.showwarning("Input Error", "Tolong isi semua data")

        # Tombol untuk submit data
        ctk.CTkButton(popup, text="Add User", command=submit_new_user).pack(pady=20)

        popup.mainloop()

    # Load data pengguna
    load_data()

    # Tombol untuk tambah user
    add_button = ctk.CTkButton(table_frame, text="Add User", command=create_popup)
    add_button.pack(side="left", padx=10, pady=10)

    # Tombol untuk hapus user
    delete_button = ctk.CTkButton(table_frame, text="Delete User", command=delete_user)
    delete_button.pack(side="left", padx=10, pady=10)

    # Tombol untuk edit user
    edit_button = ctk.CTkButton(table_frame, text="Edit User", command=edit_user)
    edit_button.pack(side="left", padx=10, pady=10)
