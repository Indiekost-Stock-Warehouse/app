import customtkinter as ctk
from tkinter import ttk

# Setup aplikasi
ctk.set_appearance_mode("Light")  # Pilihan mode: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")


class StockPageApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Halaman Stok Barang")
        self.geometry("1200x700")

        # Sidebar (Menu Navigasi)
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")
        self.sidebar_frame.grid_propagate(False)

        self.menu_label = ctk.CTkLabel(self.sidebar_frame, text="MENU", font=("Arial", 16, "bold"))
        self.menu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.dashboard_button = ctk.CTkButton(self.sidebar_frame, text="Dashboard")
        self.dashboard_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.stock_button = ctk.CTkButton(self.sidebar_frame, text="Stok Barang")
        self.stock_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.transaksi_button = ctk.CTkButton(self.sidebar_frame, text="Transaksi")
        self.transaksi_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        self.logout_button = ctk.CTkButton(self.sidebar_frame, text="Keluar", fg_color="red", hover_color="darkred")
        self.logout_button.grid(row=4, column=0, padx=20, pady=(50, 10), sticky="w")

        # Frame utama (Konten)
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self.main_frame, text="Stok Barang", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

        # Tabel Data
        self.table_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.table_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self.tree = ttk.Treeview(
            self.table_frame, 
            columns=("No", "Kode Barang", "Nama Barang", "Jumlah", "Aksi"), 
            show="headings"
        )
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Kolom tabel
        self.tree.heading("No", text="#")
        self.tree.heading("Kode Barang", text="Kode Barang")
        self.tree.heading("Nama Barang", text="Nama Barang")
        self.tree.heading("Jumlah", text="Jumlah Barang")
        self.tree.heading("Aksi", text="Aksi")

        self.tree.column("No", width=50, anchor="center")
        self.tree.column("Kode Barang", width=150, anchor="center")
        self.tree.column("Nama Barang", width=250, anchor="w")
        self.tree.column("Jumlah", width=150, anchor="center")
        self.tree.column("Aksi", width=150, anchor="center")

        # Contoh Data
        data = [
            ("1", "#098701", "Indomie Goreng", "100", "Edit | Hapus"),
            ("2", "#098701", "Indomie Goreng Cabe Ijo", "75", "Edit | Hapus"),
            ("3", "#098701", "Indomie Goreng Rendang", "50", "Edit | Hapus"),
            ("4", "#098701", "Good Day Cappuccino", "75", "Edit | Hapus"),
        ]

        for item in data:
            self.tree.insert("", "end", values=item)

        # Floating Action Button (Tambah Data)
        self.add_button = ctk.CTkButton(
            self.main_frame,
            text="+",
            width=50,
            height=50,
            corner_radius=25,
            fg_color="red",
            font=("Arial", 24, "bold"),
            hover_color="darkred",
        )
        self.add_button.place(relx=0.9, rely=0.9, anchor="center")

        # Pencarian, Filter, dan Ekspor
        self.top_bar = ctk.CTkFrame(self.main_frame, corner_radius=0, height=50)
        self.top_bar.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        self.search_entry = ctk.CTkEntry(self.top_bar, placeholder_text="Search")
        self.search_entry.pack(side="left", padx=10, pady=10)

        self.export_button = ctk.CTkButton(self.top_bar, text="Export", width=70, fg_color="blue")
        self.export_button.pack(side="right", padx=10, pady=10)

        self.filter_button = ctk.CTkButton(self.top_bar, text="Filter", width=70, fg_color="red")
        self.filter_button.pack(side="right", padx=10, pady=10)

        self.notification_button = ctk.CTkButton(
            self.top_bar, text="🔔", fg_color="transparent", width=40, font=("Arial", 20)
        )
        self.notification_button.pack(side="right", padx=10, pady=10)

        self.profile_button = ctk.CTkButton(
            self.top_bar, text="☰", fg_color="transparent", width=40, font=("Arial", 20)
        )
        self.profile_button.pack(side="right", padx=10, pady=10)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    app = StockPageApp()
    app.mainloop()
