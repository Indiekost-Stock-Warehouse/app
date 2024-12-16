import sqlite3
import customtkinter as ctk

# Membuat koneksi ke database SQLite
connection = sqlite3.connect("db_p3l.db")
cursor = connection.cursor()

# Fungsi untuk menyisipkan data ke tabel database
def insert_data(nama_barang, jumlah_barang, satuan_barang):
    try:
        cursor.execute("INSERT INTO gudang (nama, stok, satuan) VALUES (?, ?, ?)", 
                       (nama_barang, jumlah_barang, satuan_barang))
        connection.commit()
        print(f"Data berhasil ditambahkan: {nama_barang} - {jumlah_barang} - {satuan_barang}")
    except sqlite3.Error as e:
        print(f"Error menambahkan data: {e}")

# Fungsi untuk membuat dan menampilkan pop-up
def tambah_popup():
    # Membuat jendela pop-up utama
    popup = ctk.CTk()
    popup.geometry("500x250")
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
        command=lambda: add_new_data(popup, nama_entry.get(), jumlah_entry.get(), satuan_entry.get())
    )
    add_button.pack(side="bottom", pady=10)

    # Menjalankan pop-up
    popup.mainloop()

# Fungsi untuk validasi input dan menambah data baru
def add_new_data(popup, nama_barang, jumlah_barang, satuan_barang):
    if nama_barang.strip() and jumlah_barang.isdigit() and satuan_barang.strip():
        insert_data(nama_barang.strip(), int(jumlah_barang.strip()), satuan_barang.strip())
        popup.destroy()
    else:
        print("Input tidak valid. Pastikan semua field diisi dengan benar.")

# Memanggil fungsi untuk menampilkan pop-up
tambah_popup()

# Menutup koneksi database saat aplikasi selesai
connection.close()
