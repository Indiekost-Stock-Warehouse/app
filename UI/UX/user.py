import customtkinter as ctk
from tkinter import ttk

# Setup utama
ctk.set_appearance_mode("Light")  # Pilihan: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Pilihan: "blue", "green", "dark-blue"


class UserPageApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Halaman User")
        self.geometry("1200x700")

        # Frame kiri (Menu Navigasi)
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

        self.user_button = ctk.CTkButton(self.sidebar_frame, text="User")
        self.user_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.logout_button = ctk.CTkButton(self.sidebar_frame, text="Keluar", fg_color="red", hover_color="darkred")
        self.logout_button.grid(row=5, column=0, padx=20, pady=50, sticky="w")

        # Frame konten utama
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.user_label = ctk.CTkLabel(self.main_frame, text="User", font=("Arial", 20, "bold"))
        self.user_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

        # Tabel data pengguna
        self.table_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.table_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self.tree = ttk.Treeview(self.table_frame, columns=("No", "Name", "Role", "Status"), show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Kolom tabel
        self.tree.heading("No", text="#")
        self.tree.heading("Name", text="NAME")
        self.tree.heading("Role", text="ROLE")
        self.tree.heading("Status", text="STATUS")

        self.tree.column("No", width=50, anchor="center")
        self.tree.column("Name", width=200, anchor="w")
        self.tree.column("Role", width=100, anchor="center")
        self.tree.column("Status", width=100, anchor="center")

        # Contoh data tabel
        self.tree.insert("", "end", values=("1", "Miss Yuli", "Owner", "Active"))
        self.tree.insert("", "end", values=("2", "Iwan", "Admin", "Active"))

        # Tombol tambah (floating action button)
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

        # Pencarian dan filter
        self.top_bar = ctk.CTkFrame(self.main_frame, corner_radius=0, height=50)
        self.top_bar.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        self.search_entry = ctk.CTkEntry(self.top_bar, placeholder_text="Search")
        self.search_entry.pack(side="left", padx=10, pady=10)

        self.filter_button = ctk.CTkButton(self.top_bar, text="Filter", fg_color="red", width=70, hover_color="darkred")
        self.filter_button.pack(side="left", padx=10, pady=10)

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
    app = UserPageApp()
    app.mainloop()
