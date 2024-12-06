import customtkinter as ctk
from tkinter import ttk
import mpok.transaksi as transaksi

# Fungsi untuk membuat sidebar
def setup_sidebar(root):
    sidebar_frame = ctk.CTkFrame(root, width=200, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, sticky="ns")
    sidebar_frame.grid_propagate(False)

    menu_label = ctk.CTkLabel(sidebar_frame, text="MENU", font=("Arial", 16, "bold"))
    menu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    dashboard_button = ctk.CTkButton(sidebar_frame, text="Dashboard", command=lambda: transaksi.show_dashboard(root))
    dashboard_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

    stock_button = ctk.CTkButton(sidebar_frame, text="Stok Barang")
    stock_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

    transaksi_button = ctk.CTkButton(sidebar_frame, text="Transaksi")
    transaksi_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    logout_button = ctk.CTkButton(sidebar_frame, text="Keluar", fg_color="red", hover_color="darkred")
    logout_button.grid(row=4, column=0, padx=20, pady=(50, 10), sticky="w")

    return sidebar_frame

# Fungsi untuk membuat konten utama
def setup_main_content(root):
    main_frame = ctk.CTkFrame(root, corner_radius=10)
    main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=1)

    title_label = ctk.CTkLabel(main_frame, text="Stok Barang", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

    # Tabel Data
    table_frame = ctk.CTkFrame(main_frame, corner_radius=10)
    table_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

    tree = ttk.Treeview(
        table_frame, 
        columns=("No", "Kode Barang", "Nama Barang", "Jumlah"), 
        show="headings"
    )
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("No", text="#")
    tree.heading("Kode Barang", text="Kode Barang")
    tree.heading("Nama Barang", text="Nama Barang")
    tree.heading("Jumlah", text="Jumlah Barang")

    tree.column("No", width=50, anchor="center")
    tree.column("Kode Barang", width=150, anchor="center")
    tree.column("Nama Barang", width=250, anchor="w")
    tree.column("Jumlah", width=150, anchor="center")

    # Contoh Data
    data = [
        ("1", "#098701", "Indomie Goreng", "100"),
        ("2", "#098702", "Indomie Goreng Cabe Ijo", "75"),
        ("3", "#098703", "Indomie Goreng Rendang", "50"),
        ("4", "#098704", "Good Day Cappuccino", "75"),
    ]

    for item in data:
        tree.insert("", "end", values=item)

    # Area Tombol Aksi
    action_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="lightgray")
    action_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

    edit_button = ctk.CTkButton(action_frame, text="Edit", state="disabled", command=lambda: edit_action(tree))
    edit_button.grid(row=0, column=0, padx=10, pady=10)

    delete_button = ctk.CTkButton(action_frame, text="Hapus", state="disabled", command=lambda: delete_action(tree))
    delete_button.grid(row=0, column=1, padx=10, pady=10)

    # Fungsi untuk mengaktifkan tombol saat baris dipilih
    def on_row_selected(event):
        selected_item = tree.selection()
        if selected_item:
            edit_button.configure(state="normal")
            delete_button.configure(state="normal")
        else:
            edit_button.configure(state="disabled")
            delete_button.configure(state="disabled")

    tree.bind("<<TreeviewSelect>>", on_row_selected)

    return main_frame

# Fungsi untuk aksi edit
def edit_action(tree):
    selected_item = tree.selection()
    if selected_item:
        item_data = tree.item(selected_item, "values")
        print(f"Edit: {item_data}")  # Ganti dengan fungsi edit yang lebih kompleks

# Fungsi untuk aksi hapus
def delete_action(tree):
    selected_item = tree.selection()
    if selected_item:
        item_data = tree.item(selected_item, "values")
        print(f"Hapus: {item_data}")  # Ganti dengan konfirmasi sebelum menghapus
        tree.delete(selected_item)

# Fungsi utama untuk setup GUI
def main(app):
    for widget in app.winfo_children():
        widget.destroy()

    app.title("Halaman Stok Barang")
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    ctk.set_appearance_mode("Light")  # Pilihan mode: "System", "Light", "Dark"
    ctk.set_default_color_theme("blue")

    setup_sidebar(app)
    setup_main_content(app)

    app.mainloop()