import customtkinter as ctk
import mpok.order as adminorder
import mpok.stok as adminstok
import mpok.transaksi as admintransaksi
import mpok.user as adminuser

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
        ("Transaksi", 4, {"command": lambda:admintransaksi.main(root)} ),
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

    # Stat Cards
    stat_card_1 = ctk.CTkFrame(main_frame, width=200, height=100, corner_radius=10)
    stat_card_1.grid(row=1, column=0, padx=20, pady=10)
    stat_card_1.grid_propagate(False)

    stat_label_1 = ctk.CTkLabel(stat_card_1, text="Total Transaksi\n2,315", font=("Arial", 14))
    stat_label_1.pack(expand=True)

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

def setup_right_panel(root):
    right_panel = ctk.CTkFrame(root, width=250, corner_radius=10)
    right_panel.grid(row=0, column=2, sticky="ns", padx=(0, 20), pady=20)

    right_panel_label = ctk.CTkLabel(right_panel, text="Aktivitas", font=("Arial", 18, "bold"))
    right_panel_label.pack(pady=20)

    aktivitas = [
        "Submit sebuah transaksi.\nBaru saja",
        "Submit stok barang.\n2 jam yang lalu"
    ]

    for item in aktivitas:
        label = ctk.CTkLabel(right_panel, text=item, font=("Arial", 14))
        label.pack(pady=10)

def main(app):
    for widget in app.winfo_children():
        widget.destroy()

    app.title("IndiKost Admin Dashboard")

    setup_sidebar(app)
    setup_main_content(app)
    setup_right_panel(app)

    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    app.mainloop()

if __name__ == "__main__":
    app = ctk.CTk()
    main(app)