import tkinter as tk
import customtkinter as ctk

# Inisialisasi root window sebagai popup
root = ctk.CTk()
root.geometry("600x400")
root.title("Stok Tersedia")

# Menambahkan judul
title_label = ctk.CTkLabel(root, text="Stok Tersedia", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=10)

# Menambahkan kolom header
header_1 = ctk.CTkLabel(root, text="#", width=50)
header_1.grid(row=1, column=0, padx=5, pady=5)

header_2 = ctk.CTkLabel(root, text="KODE BARANG", width=150)
header_2.grid(row=1, column=1, padx=5, pady=5)

header_3 = ctk.CTkLabel(root, text="NAMA BARANG", width=200)
header_3.grid(row=1, column=2, padx=5, pady=5)

header_4 = ctk.CTkLabel(root, text="JUMLAH BARANG TERSISA", width=150)
header_4.grid(row=1, column=3, padx=5, pady=5)

# Menambahkan data barang (dummy)
data = [
    ("1", "#098701", "Indomie Goreng Sambel Matah", "10"),
    ("1", "#098702", "Indomie Goreng Iga Penyet", "27"),
    ("1", "#098703", "Indomie Goreng Rendang", "38"),
    ("1", "#098704", "Indomie Goreng Cabe Ijo", "48"),
    ("1", "#098705", "Indomie Goreng Ayam Geprek", "60"),
    ("1", "#098706", "Indomie Goreng Aceh", "67"),
    ("1", "#098707", "Indomie Goreng", "86"),
]

# Menambahkan data ke dalam grid
for i, (col1, col2, col3, col4) in enumerate(data, start=2):
    ctk.CTkLabel(root, text=col1, width=50).grid(row=i, column=0, padx=5, pady=5)
    ctk.CTkLabel(root, text=col2, width=150).grid(row=i, column=1, padx=5, pady=5)
    ctk.CTkLabel(root, text=col3, width=200).grid(row=i, column=2, padx=5, pady=5)
    ctk.CTkLabel(root, text=col4, width=150).grid(row=i, column=3, padx=5, pady=5)

# Menjalankan event loop
root.mainloop()
