import customtkinter as ctk

# Setup utama
ctk.set_appearance_mode("Light")  # Pilihan: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Pilihan: "blue", "green", "dark-blue"

class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dashboard Admin")
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

        self.dashboard_title = ctk.CTkLabel(self.main_frame, text="Dashboard", font=("Arial", 20, "bold"))
        self.dashboard_title.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

        # Stat Card 1
        self.stat_card_1 = ctk.CTkFrame(self.main_frame, width=200, height=100, corner_radius=10)
        self.stat_card_1.grid(row=1, column=0, padx=20, pady=10)
        self.stat_card_1.grid_propagate(False)

        stat_label_1 = ctk.CTkLabel(self.stat_card_1, text="Total Transaksi\n2,315", font=("Arial", 14))
        stat_label_1.pack(expand=True)

        # Stat Card 2
        self.stat_card_2 = ctk.CTkFrame(self.main_frame, width=200, height=100, corner_radius=10)
        self.stat_card_2.grid(row=1, column=1, padx=20, pady=10)
        self.stat_card_2.grid_propagate(False)

        stat_label_2 = ctk.CTkLabel(self.stat_card_2, text="Total Stok\n7,265", font=("Arial", 14))
        stat_label_2.pack(expand=True)

        # Chart Placeholder
        self.chart_frame = ctk.CTkFrame(self.main_frame, height=300, corner_radius=10)
        self.chart_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        chart_label = ctk.CTkLabel(self.chart_frame, text="Chart Placeholder", font=("Arial", 16))
        chart_label.pack(expand=True)

        # Panel kanan (Aktivitas)
        self.right_panel = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.right_panel.grid(row=0, column=2, sticky="ns", padx=(0, 20), pady=20)

        right_panel_label = ctk.CTkLabel(self.right_panel, text="Aktivitas", font=("Arial", 18, "bold"))
        right_panel_label.pack(pady=20)

        aktivitas_1 = ctk.CTkLabel(self.right_panel, text="Submit sebuah transaksi.\nBaru saja", font=("Arial", 14))
        aktivitas_1.pack(pady=10)

        aktivitas_2 = ctk.CTkLabel(self.right_panel, text="Submit stok barang.\n2 jam yang lalu", font=("Arial", 14))
        aktivitas_2.pack(pady=10)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
