import customtkinter as ctk

def create_popup():
    # Membuat jendela pop-up utama
    popup = ctk.CTk()
    popup.geometry("600x250")
    popup.title("Transaksi")
    popup.resizable(False, False)

    # Bagian atas pop-up
    top_frame = ctk.CTkFrame(popup, height=50, fg_color="lightgray", corner_radius=0)
    top_frame.pack(side="top", fill="x")

    title_label = ctk.CTkLabel(top_frame, text="Transaksi", font=("Arial", 16, "bold"))
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

    # Input Tanggal Pemesanan
    tgl_label = ctk.CTkLabel(content_frame, text="Tgl Pemesanan:", anchor="w")
    tgl_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    tgl_entry = ctk.CTkEntry(content_frame, placeholder_text="15/11/2024")
    tgl_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Input Pesanan
    pesanan_label = ctk.CTkLabel(content_frame, text="Pesanan:", anchor="w")
    pesanan_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    pesanan_entry = ctk.CTkEntry(content_frame, placeholder_text="Mie Tektek Goreng")
    pesanan_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Input Jumlah Pesanan
    jumlah_label = ctk.CTkLabel(content_frame, text="Jumlah Pesanan:", anchor="w")
    jumlah_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    jumlah_entry = ctk.CTkEntry(content_frame, placeholder_text="25")
    jumlah_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Mengatur kolom agar dapat di-resize
    content_frame.grid_columnconfigure(1, weight=1)

    # Tombol Selanjutnya
    next_button = ctk.CTkButton(
        popup,
        text="Selanjutnya",
        fg_color="red",
        hover_color="darkred",
        corner_radius=10,
        command=lambda: print(f"Tanggal: {tgl_entry.get()}, Pesanan: {pesanan_entry.get()}, Jumlah: {jumlah_entry.get()}")
    )
    next_button.pack(side="bottom", pady=2)

    # Menjalankan pop-up
    popup.mainloop()

# Memanggil fungsi untuk menampilkan pop-up
create_popup()
