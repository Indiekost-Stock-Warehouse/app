import customtkinter as ctk

# Fungsi untuk membuat dan menampilkan pop-up
def create_popup():
    # Membuat jendela pop-up utama
    popup = ctk.CTk()
    popup.geometry("500x200")
    popup.title("Hapus Data")
    popup.resizable(False, False)

    # Bagian atas pop-up
    top_frame = ctk.CTkFrame(popup, height=50, fg_color="lightgray", corner_radius=0)
    top_frame.pack(side="top", fill="x")

    title_label = ctk.CTkLabel(top_frame, text="Hapus Data", font=("Arial", 16, "bold"))
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
    nama_entry = ctk.CTkEntry(content_frame, placeholder_text="Good Day Vanilla Latte")
    nama_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Input Jumlah Barang
    jumlah_label = ctk.CTkLabel(content_frame, text="Jumlah Barang:", anchor="w")
    jumlah_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    jumlah_entry = ctk.CTkEntry(content_frame, placeholder_text="75")
    jumlah_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    content_frame.grid_columnconfigure(1, weight=1)

    # Tombol Tambah Barang
    add_button = ctk.CTkButton(
        popup,
        text="Hapus Barang",
        fg_color="red",
        hover_color="darkred",
        corner_radius=10,
        command=lambda: print(f"Barang: {nama_entry.get()}, Jumlah: {jumlah_entry.get()}")
    )
    add_button.pack(side="bottom", pady=2)

    # Menjalankan pop-up
    popup.mainloop()

# Memanggil fungsi untuk menampilkan pop-up
create_popup()
