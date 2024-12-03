import customtkinter as ctk
from tkinter import ttk
import mpok.transaksi as transaksi

# Setup utama
def setup_app(app):
    # Clear previous widgets
    for widget in app.winfo_children():
        widget.destroy()

    setup_sidebar(app)
    main_frame = setup_main_content(app)

    setup_top_bar(main_frame)
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

    menu_items = [("Dashboard", lambda: transaksi.show_dashboard(root)), 
                  ("Stok Barang", lambda: print("Stok Barang diklik")),
                  ("Transaksi", lambda: print("Transaksi diklik")),
                  ("User", lambda: print("User diklik"))
                  ]
    
    for i, (item, action) in enumerate(menu_items, start=1):
        button = ctk.CTkButton(sidebar_frame, text=item, command=action or (lambda: None))
        button.grid(row=i, column=0, padx=20, pady=10, sticky="w")

    logout_button = ctk.CTkButton(sidebar_frame, text="Keluar", fg_color="red", hover_color="darkred")
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

    profile_button = ctk.CTkButton(
        top_bar, text="☰", fg_color="transparent", width=40, font=("Arial", 20)
    )
    profile_button.pack(side="right", padx=10, pady=10)

    notification_button = ctk.CTkButton(
        top_bar, text="🔔", fg_color="transparent", width=40, font=("Arial", 20)
    )
    notification_button.pack(side="right", padx=10, pady=10)

# Tabel data pengguna
def setup_user_table(main_frame):
    table_frame = ctk.CTkFrame(main_frame, corner_radius=10)
    table_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

    tree = ttk.Treeview(table_frame, columns=("No", "Name", "Role", "Status"), show="headings")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("No", text="#")
    tree.heading("Name", text="NAME")
    tree.heading("Role", text="ROLE")
    tree.heading("Status", text="STATUS")

    tree.column("No", width=50, anchor="center")
    tree.column("Name", width=200, anchor="w")
    tree.column("Role", width=100, anchor="center")
    tree.column("Status", width=100, anchor="center")

    # Contoh data
    data = [
        ("1", "Miss Yuli", "Owner", "Active"),
        ("2", "Iwan", "Admin", "Active"),
    ]

    for item in data:
        tree.insert("", "end", values=item)

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
    )
    add_button.place(relx=0.9, rely=0.9, anchor="center")