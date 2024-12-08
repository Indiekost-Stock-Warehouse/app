import customtkinter as ctk
from tkinter import ttk , messagebox
import sqlite3
import mpok.dashboard as adminlogin
import mpok.order as adminorder
import mpok.transaksi as admintransaksi
import mpok.user as adminuser

connection = sqlite3.connect("db_p3l.db")
cursor = connection.cursor()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 4
    window.geometry(f"{width}x{height}+{x}+{y}")

# Fungsi untuk mengambil data dari database SQLite
def fetch_data_from_db():
    cursor.execute("SELECT id, nama, stok, satuan FROM gudang")
    data = cursor.fetchall()
    return data

# Fungsi untuk menyisipkan data ke tabel database
def insert_data(nama_barang, jumlah_barang, satuan_barang):
    try:
        cursor.execute("INSERT INTO gudang (nama, stok, satuan) VALUES (?, ?, ?)", 
                       (nama_barang, jumlah_barang, satuan_barang))
        connection.commit()
    except sqlite3.Error as e:
        messagebox.showwarning("Input Error", "Input tidak valid. Pastikan semua field diisi dengan benar.")(f"Error menambahkan data: {e}")

def refresh_table(tree):
    # Hapus semua data di Treeview
    for row in tree.get_children():
        tree.delete(row)
    
    # Ambil data terbaru dari database
    data = fetch_data_from_db()
    
    # Tambahkan data terbaru ke Treeview
    for item in data:
        tree.insert("", "end", values=item)

# Fungsi untuk membuat dan menampilkan pop-up
def tambah_popup():
    # Membuat jendela pop-up utama
    popup = ctk.CTk()
    center_window(popup, 500, 250)

    popup.title("Tambah Data")
    popup.resizable(False, False)

    # Bagian atas pop-up
    top_frame = ctk.CTkFrame(popup, height=50, fg_color="lightgray", corner_radius=0)
    top_frame.pack(side="top", fill="x")

    title_label = ctk.CTkLabel(top_frame, text="Tambah Data", font=("Arial", 16, "bold"))
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
    content_frame = ctk.CTkFrame(popup, fg_color="white", corner_radius=10)
    content_frame.pack(side="top", fill="both", expand=True, padx=20, pady=10)

    # Input Nama Barang
    nama_label = ctk.CTkLabel(content_frame, text="Nama Barang:", anchor="w")
    nama_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    nama_entry = ctk.CTkEntry(content_frame, placeholder_text="Nama Barang")
    nama_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Input Jumlah Barang
    jumlah_label = ctk.CTkLabel(content_frame, text="Jumlah Barang:", anchor="w")
    jumlah_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    jumlah_entry = ctk.CTkEntry(content_frame, placeholder_text="Jumlah")
    jumlah_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Input Satuan Barang
    satuan_label = ctk.CTkLabel(content_frame, text="Satuan Barang:", anchor="w")
    satuan_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    satuan_entry = ctk.CTkEntry(content_frame, placeholder_text="KG / Liter")
    satuan_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    content_frame.grid_columnconfigure(1, weight=1)

    # Tombol Tambah Barang
    add_button = ctk.CTkButton(
        popup,
        text="Tambah Barang",
        fg_color="green",
        hover_color="darkgreen",
        corner_radius=10,
        command=lambda: add_new_data(popup, nama_entry.get(), jumlah_entry.get(), satuan_entry.get(), tree)
    )
    add_button.pack(side="bottom", pady=10)
    # Menjalankan pop-up
    popup.mainloop()

# Fungsi untuk validasi input dan menambah data baru
def add_new_data(popup, nama_barang, jumlah_barang, satuan_barang, tree):
    if nama_barang.strip() and jumlah_barang.isdigit() and satuan_barang.strip():
        insert_data(nama_barang.strip(), int(jumlah_barang.strip()), satuan_barang.strip())
        
        # Refresh data di Treeview
        refresh_table(tree)
        
        messagebox.showinfo("Success", f"Data berhasil ditambahkan: {nama_barang} - {jumlah_barang} - {satuan_barang}")
        popup.destroy()
    else:
        messagebox.showwarning("Input Error", "Input tidak valid. Pastikan semua field diisi dengan benar.")

def update_db(item_id, nama_baru, jumlah_baru, satuan_baru):
    cursor.execute(
        "UPDATE gudang SET nama = ?, stok = ?, satuan = ? WHERE id = ?",
        (nama_baru, jumlah_baru, satuan_baru, item_id)
    )
    connection.commit()

 #Fungsi untuk menampilkan pop-up edit data
def edit_popup(item_id, current_name, current_stok, current_satuan):
    # Membuat jendela pop-up utama
    popup = ctk.CTk()
    center_window(popup, 500, 300)
    popup.title("Edit Data")
    popup.resizable(False, False)

    # Bagian atas pop-up
    top_frame = ctk.CTkFrame(popup, height=50, fg_color="lightgray", corner_radius=0)
    top_frame.pack(side="top", fill="x")

    title_label = ctk.CTkLabel(top_frame, text="Edit Data", font=("Arial", 16, "bold"))
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
    content_frame = ctk.CTkFrame(popup, fg_color="white", corner_radius=10)
    content_frame.pack(side="top", fill="both", expand=True, padx=20, pady=10)

    # Input Nama Barang
    nama_label = ctk.CTkLabel(content_frame, text="Nama Barang:", anchor="w")
    nama_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    nama_entry = ctk.CTkEntry(content_frame, placeholder_text="Nama Barang")
    nama_entry.insert(0, current_name)  # Isi dengan data lama
    nama_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Input Jumlah Barang
    jumlah_label = ctk.CTkLabel(content_frame, text="Jumlah Stock:", anchor="w")
    jumlah_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    jumlah_entry = ctk.CTkEntry(content_frame, placeholder_text="Jumlah Stock")
    jumlah_entry.insert(0, str(current_stok))  # Isi dengan data lama
    jumlah_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Input Satuan Barang
    satuan_label = ctk.CTkLabel(content_frame, text="Satuan:", anchor="w")
    satuan_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    satuan_entry = ctk.CTkEntry(content_frame, placeholder_text="Satuan Barang")
    satuan_entry.insert(0, current_satuan)  # Isi dengan data lama
    satuan_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    content_frame.grid_columnconfigure(1, weight=1)

    # Tombol Simpan Perubahan
    save_button = ctk.CTkButton(
        popup,
        text="Simpan Perubahan",
        fg_color="green",
        hover_color="darkgreen",
        corner_radius=10,
        command=lambda: save_changes(popup, item_id, nama_entry.get(), jumlah_entry.get(), satuan_entry.get())
    )
    save_button.pack(side="bottom", pady=10)

    # Menjalankan pop-up
    popup.mainloop()

#Fungsi untuk menyimpan perubahan ke database
def save_changes(popup, item_id, nama_baru, jumlah_baru, satuan_baru):
    if nama_baru.strip() and jumlah_baru.strip().isdigit() and satuan_baru.strip():
        update_db(item_id, nama_baru.strip(), int(jumlah_baru.strip()), satuan_baru.strip())
        popup.destroy()
        messagebox.showinfo("Success", f"Item dengan ID {item_id} berhasil diperbarui.")
    else:
        messagebox.showerror("Input Error", "Input tidak valid. Periksa kembali data yang dimasukkan.")


# Fungsi untuk menghapus data dari database SQLite
def delete_from_db(item_id):
    cursor.execute("DELETE FROM gudang WHERE id = ?", (item_id,))
    connection.commit()

# Fungsi untuk membuat sidebar
def setup_sidebar(root):
    sidebar_frame = ctk.CTkFrame(root, width=200, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, sticky="ns")
    sidebar_frame.grid_propagate(False)

    menu_label = ctk.CTkLabel(sidebar_frame, text="MENU", font=("Arial", 16, "bold"))
    menu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    dashboard_button = ctk.CTkButton(sidebar_frame, text="Dashboard", command=lambda: adminlogin.main(root))
    dashboard_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

    dashboard_button = ctk.CTkButton(sidebar_frame, text="Pesanan", command=lambda: adminorder.lihat_order(root))
    dashboard_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

    stock_button = ctk.CTkButton(sidebar_frame, text="Stok Barang", fg_color="green")
    stock_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    transaksi_button = ctk.CTkButton(sidebar_frame, text="Transaksi", command = lambda: admintransaksi.main(root))
    transaksi_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

    logout_button = ctk.CTkButton(sidebar_frame, text="Users", command=lambda: adminuser.setup_app(root), fg_color="purple")
    logout_button.grid(row=5, column=0, padx=20, pady=(50, 10), sticky="w")

    return sidebar_frame

def setup_floating_button(root):
    add_button = ctk.CTkButton(
        root,
        text="+",
        width=50,
        height=50,
        corner_radius=25,
        fg_color="red",
        font=("Arial", 24, "bold"),
        hover_color="darkred",
        command=lambda: tambah_popup(),
    )
    add_button.place(relx=0.87, rely=0.75, anchor="center")

# Setup Main Content
def setup_main_content(root):
    main_frame = ctk.CTkFrame(root, corner_radius=10)
    main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=1)
    setup_floating_button(root)

    title_label = ctk.CTkLabel(main_frame, text="Stok Barang", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

    # Tabel Data
    table_frame = ctk.CTkFrame(main_frame, corner_radius=10)
    table_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

    global tree
    tree = ttk.Treeview(
        table_frame,
        columns=("ID", "Nama", "Stok", "Satuan"),
        show="headings"
    )
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Nama", text="Nama")
    tree.heading("Stok", text="Stok")
    tree.heading("Satuan", text="Satuan")

    tree.column("ID", width=50, anchor="center")
    tree.column("Nama", width=250, anchor="w")
    tree.column("Stok", width=100, anchor="center")
    tree.column("Satuan", width=100, anchor="center")

    # Mengisi data dari database ke Treeview
    data = fetch_data_from_db()
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
    def on_row_selected(event): #jgn hapus argumen event nya
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
        item_id = item_data[0]  # ID dari kolom pertama
        current_name = item_data[1]
        current_stok = item_data[2]
        current_satuan = item_data[3]
        edit_popup(item_id, current_name, current_stok, current_satuan)

# Fungsi untuk aksi hapus
def delete_action(tree):
    selected_item = tree.selection()
    if selected_item:
        item_data = tree.item(selected_item, "values")
        item_id = item_data[0]  # ID adalah kolom pertama
        confirm = messagebox.askyesno("Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus data ini?")
        if confirm :
            try:
                delete_from_db(item_id)
                tree.delete(selected_item)
                messagebox.showinfo("Success", f"Item dengan ID {item_id} berhasil dihapus.")
            except sqlite3.Error as e:
                messagebox.showerror("Failed", "Database Error", f"Error deleting data: {e}")

# Fungsi utama untuk setup GUI
def main_ui(app):
    for widget in app.winfo_children():
        widget.destroy()

    app.title("IndieKost Stock List")
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    setup_sidebar(app)
    setup_main_content(app)

    app.mainloop()
    connection.close()

if __name__ == "__main__":
    main_ui(ctk.CTk())