import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
import mpok.order as adminorder
import mpok.stok as adminstok
import mpok.transaksi as admintransaksi
import mpok.user as adminuser
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk membuat chart
def display_sales_chart(chart_frame):
    # Hapus widget sebelumnya dalam chart_frame
    for widget in chart_frame.winfo_children():
        widget.destroy()

    today = datetime.now().strftime("%Y-%m-%d")
    file_path = f"./report/sell/{today}.xlsx"

    try:
        # Membaca file Excel
        data = pd.read_excel(file_path)
        
        if data.empty:
            raise ValueError("Data penjualan kosong")

        # Menghitung total jumlah penjualan per barang
        sales_summary = data.groupby("Barang Pesanan")["Jumlah"].sum().sort_values(ascending=False).head(10)

        # Membuat chart menggunakan matplotlib
        fig, ax = plt.subplots(figsize=(8, 4))
        sales_summary.plot(kind="bar", ax=ax, color="skyblue")
        ax.set_title("Barang Terlaris Hari Ini", fontsize=14)
        ax.set_xlabel("Barang Pesanan")
        ax.set_ylabel("Jumlah Terjual")
        ax.tick_params(axis='x', rotation=45)
        
        # Menampilkan chart di Tkinter
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    except FileNotFoundError:
        label = ctk.CTkLabel(chart_frame, text="Belum ada penjualan hari ini", font=("Arial", 14))
        label.pack(expand=True)
    except ValueError:
        label = ctk.CTkLabel(chart_frame, text="Data penjualan kosong", font=("Arial", 14))
        label.pack(expand=True)

# Fungsi untuk mendapatkan statistik penjualan dan pembelian
def get_stats():
    today = datetime.now().strftime("%Y-%m-%d")
    sell_path = f"./report/sell/{today}.xlsx"
    buy_path = f"./report/buy/{today}.xlsx"

    try:
        # Membaca data penjualan
        sell_data = pd.read_excel(sell_path)
        total_sales = len(sell_data) if not sell_data.empty else 0  # Jumlah baris = jumlah transaksi
    except FileNotFoundError:
        total_sales = 0  # Jika file tidak ditemukan, set jumlah transaksi penjualan = 0

    try:
        # Membaca data pembelian
        buy_data = pd.read_excel(buy_path)
        total_purchases = len(buy_data) if not buy_data.empty else 0  # Jumlah baris = jumlah transaksi
    except FileNotFoundError:
        total_purchases = 0  # Jika file tidak ditemukan, set jumlah transaksi pembelian = 0

    return total_sales, total_purchases


def setup_sidebar(root):
    sidebar_frame = ctk.CTkFrame(root, width=200, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, sticky="ns")
    sidebar_frame.grid_propagate(False)

    menu_label = ctk.CTkLabel(sidebar_frame, text="MENU", font=("Arial", 16, "bold"))
    menu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    buttons = [
        ("Dashboard", 1, {"fg_color": "green"}),
        ("Pesanan", 2, {"command": lambda: adminorder.lihat_order(root)} ),
        ("Stok Barang", 3, {"command": lambda: adminstok.main_ui(root)} ),
        ("Riwayat Transaksi", 4, {"command": lambda:admintransaksi.main(root)} ),
        ("Users", 5, {"command": lambda:adminuser.setup_app(root), "fg_color": "purple"}),
    ]

    for text, row, *opts in buttons:
        options = opts[0] if opts else {}
        button = ctk.CTkButton(sidebar_frame, text=text, **options)
        button.grid(row=row, column=0, padx=20, pady=10 if text != "Keluar" else 50, sticky="w")

def setup_main_content(root):
    main_frame = ctk.CTkFrame(root, corner_radius=10)
    main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(2, weight=1)

    dashboard_title = ctk.CTkLabel(main_frame, text="Dashboard", font=("Arial", 20, "bold"))
    dashboard_title.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

    # Ambil statistik penjualan dan pembelian
    total_sales, total_purchases = get_stats()

    # Stat Cards
    # Card untuk Penjualan
    stat_card_1 = ctk.CTkFrame(main_frame, width=200, height=100, corner_radius=50, fg_color="transparent")  # Menghilangkan warna latar belakang abu-abu
    stat_card_1.grid(row=1, column=0, padx=20, pady=10)
    stat_card_1.grid_propagate(False)

    stat_label_1 = ctk.CTkLabel(stat_card_1, text=f"Total Penjualan\n{total_sales}", font=("Arial", 14), anchor="center")  # Teks dipusatkan
    stat_label_1.pack(expand=True)

    # Card untuk Pembelian
    stat_card_2 = ctk.CTkFrame(main_frame, width=200, height=100, corner_radius=50, fg_color="transparent")  # Menghilangkan warna latar belakang abu-abu
    stat_card_2.grid(row=1, column=1, padx=20, pady=10)
    stat_card_2.grid_propagate(False)

    stat_label_2 = ctk.CTkLabel(stat_card_2, text=f"Total Pembelian\n{total_purchases}", font=("Arial", 14), anchor="center")  # Teks dipusatkan
    stat_label_2.pack(expand=True)


    # Chart Placeholder
    chart_frame = ctk.CTkFrame(main_frame, height=300, corner_radius=10)
    chart_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    display_sales_chart(chart_frame)

def main(app):
    for widget in app.winfo_children():
        widget.destroy()

    app.title("IndieKost Admin Dashboard")

    setup_sidebar(app)
    setup_main_content(app)

    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    app.mainloop()

if __name__ == "__main__":
    app = ctk.CTk()
    main(app)