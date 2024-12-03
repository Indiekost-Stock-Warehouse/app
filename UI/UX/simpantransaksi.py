import customtkinter as ctk

def create_popup():
    # Membuat jendela pop-up utama
    popup = ctk.CTk()
    popup.geometry("700x200")
    popup.title("Transaksi")
    popup.resizable(False, False)

    # Konten pop-up
    content_frame = ctk.CTkFrame(popup, fg_color="white", corner_radius=10)
    content_frame.pack(side="top", fill="both", expand=True, padx=20, pady=10)

    # Header tabel
    header_frame = ctk.CTkFrame(content_frame, fg_color="lightgray", corner_radius=10)
    header_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    header_labels = ["#", "TGL PEMESANAN", "NAMA PESANAN", "JUMLAH PESANAN"]
    for col, text in enumerate(header_labels):
        label = ctk.CTkLabel(header_frame, text=text, anchor="center", font=("Arial", 12, "bold"))
        label.grid(row=0, column=col, padx=10, pady=5)

    # Isi tabel
    data_frame = ctk.CTkFrame(content_frame, fg_color="white", corner_radius=10)
    data_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    data = ["1", "15/11/2024", "Mie Tektek Goreng", "25"]
    for col, text in enumerate(data):
        label = ctk.CTkLabel(data_frame, text=text, anchor="center", font=("Arial", 12))
        label.grid(row=0, column=col, padx=10, pady=5)

    # Tombol Simpan
    save_button = ctk.CTkButton(
        popup,
        text="Simpan",
        fg_color="red",
        hover_color="darkred",
        corner_radius=10,
        command=popup.destroy  # Tutup pop-up
    )
    save_button.pack(side="bottom", pady=10, padx=20)

    # Menjalankan pop-up
    popup.mainloop()

# Memanggil fungsi untuk menampilkan pop-up
create_popup()
