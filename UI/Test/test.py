import customtkinter as ctk

# Setup utama
ctk.set_appearance_mode("Light")  # Pilihan: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Pilihan: "blue", "green", "dark-blue"

# Membuat jendela utama
app = ctk.CTk()
app.title("Dashboard Admin")
app.geometry("1200x700")

# Frame kiri (Menu Navigasi)
sidebar_frame = ctk.CTkFrame(app, width=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky="ns")
sidebar_frame.grid_propagate(False)

menu_label = ctk.CTkLabel(sidebar_frame, text="MENU", font=("Arial", 16, "bold"))
menu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

dashboard_button = ctk.CTkButton(sidebar_frame, text="Dashboard", command=lambda: print("Dashboard Button clicked"))
dashboard_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

stock_button = ctk.CTkButton(sidebar_frame, text="Stok Barang", command=lambda: print("Stok Barang Button clicked"))
stock_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

transaksi_button = ctk.CTkButton(sidebar_frame, text="Transaksi", command=lambda: print("Transaksi Button clicked"))
transaksi_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

user_button = ctk.CTkButton(sidebar_frame, text="User", command=lambda: print("User Button clicked"))
user_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

logout_button = ctk.CTkButton(sidebar_frame, text="Keluar", fg_color="red", hover_color="darkred", command=app.quit)
logout_button.grid(row=5, column=0, padx=20, pady=50, sticky="w")

# Frame konten utama
main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

dashboard_title = ctk.CTkLabel(main_frame, text="Dashboard", font=("Arial", 20, "bold"))
dashboard_title.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

# Stat Card 1
stat_card_1 = ctk.CTkFrame(main_frame, width=200, height=100, corner_radius=10)
stat_card_1.grid(row=1, column=0, padx=20, pady=10)
stat_card_1.grid_propagate(False)

stat_label_1 = ctk.CTkLabel(stat_card_1, text="Total Transaksi\n2,315", font=("Arial", 14))
stat_label_1.pack(expand=True)

# Stat Card 2
stat_card_2 = ctk.CTkFrame(main_frame, width=200, height=100, corner_radius=10)
stat_card_2.grid(row=1, column=1, padx=20, pady=10)
stat_card_2.grid_propagate(False)

stat_label_2 = ctk.CTkLabel(stat_card_2, text="Total Stok\n7,265", font=("Arial", 14))
stat_label_2.pack(expand=True)

# Chart Placeholder
chart_frame = ctk.CTkFrame(main_frame, height=300, corner_radius=10)
chart_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

chart_label = ctk.CTkLabel(chart_frame, text="Chart Placeholder", font=("Arial", 16))
chart_label.pack(expand=True)

# Panel kanan (Aktivitas)
right_panel = ctk.CTkFrame(app, width=250, corner_radius=10)
right_panel.grid(row=0, column=2, sticky="ns", padx=(0, 20), pady=20)

right_panel_label = ctk.CTkLabel(right_panel, text="Aktivitas", font=("Arial", 18, "bold"))
right_panel_label.pack(pady=20)

aktivitas_1 = ctk.CTkLabel(right_panel, text="Submit sebuah transaksi.\nBaru saja", font=("Arial", 14))
aktivitas_1.pack(pady=10)

aktivitas_2 = ctk.CTkLabel(right_panel, text="Submit stok barang.\n2 jam yang lalu", font=("Arial", 14))
aktivitas_2.pack(pady=10)

# Mengatur grid weight
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Menjalankan aplikasi
app.mainloop()
