from customtkinter import *

# Inisialisasi window utama
app = CTk()
app.geometry("500x300")
app.title("Filter Popup Example")

# Fungsi untuk tombol Reset
def reset_fields():
    kode_barang_entry.delete(0, "end")
    nama_barang_entry.delete(0, "end")
    satuan_combobox.set("")

# Fungsi untuk tombol Search
def search_items():
    kode_barang = kode_barang_entry.get()
    nama_barang = nama_barang_entry.get()
    satuan = satuan_combobox.get()
    print(f"Searching for: {kode_barang}, {nama_barang}, {satuan}")

# Frame untuk konten utama (mirip dengan pop-up dalam gambar)
popup_frame = CTkFrame(app, width=400, height=200, corner_radius=10)
popup_frame.pack(pady=20, padx=20)

# Label dan input Kode Barang
kode_barang_label = CTkLabel(popup_frame, text="Kode Barang")
kode_barang_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
kode_barang_entry = CTkEntry(popup_frame, placeholder_text="#000001")
kode_barang_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Label dan input Nama Barang
nama_barang_label = CTkLabel(popup_frame, text="Nama Barang")
nama_barang_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")
nama_barang_entry = CTkEntry(popup_frame, placeholder_text="Indomie")
nama_barang_entry.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

# Label dan Combobox Satuan
satuan_label = CTkLabel(popup_frame, text="Satuan")
satuan_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
satuan_combobox = CTkComboBox(popup_frame, values=["Pcs", "Box", "Lusin"])
satuan_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Frame untuk tombol
button_frame = CTkFrame(popup_frame)
button_frame.grid(row=2, column=0, columnspan=4, pady=10)

# Tombol Reset
reset_button = CTkButton(button_frame, text="Reset", width=100, fg_color="red", hover_color="darkred", command=reset_fields)
reset_button.pack(side="left", padx=10)

# Tombol Search
search_button = CTkButton(button_frame, text="Search", width=100, fg_color="green", hover_color="darkgreen", command=search_items)
search_button.pack(side="right", padx=10)

# Pengaturan grid untuk frame utama agar kolom menyesuaikan ukuran
popup_frame.grid_columnconfigure(1, weight=1)
popup_frame.grid_columnconfigure(3, weight=1)

# Menjalankan aplikasi
app.mainloop()
