import customtkinter as ctk
from tkinter import ttk, messagebox
import os
import datetime
import pandas as pd
import mpok.dashboard as adminlogin
import mpok.order as adminorder
import mpok.stok as adminstok
import mpok.user as adminuser

def main(app):
    global orders_data, table
    for widget in app.winfo_children():
        widget.destroy()

    # create the main window
    app.title("Indiekost History Transaksi")

    # create the sidebar
    sidebar_frame = ctk.CTkFrame(app, width=140, corner_radius=0)
    sidebar_frame.pack(side="left", fill="y")

    menu_label = ctk.CTkLabel(sidebar_frame, text="MENU", font=("Arial", 16, "bold"))
    menu_label.pack(pady=5, padx=10)

    # create the sidebar buttons
    dashboard_button = ctk.CTkButton(sidebar_frame, text="Dashboard", command=lambda: adminlogin.main(app))
    dashboard_button.pack(pady=5, padx=10)
    
    order_button = ctk.CTkButton(sidebar_frame, text="Pesanan", command=lambda: adminorder.lihat_order(app))
    order_button.pack(pady=5, padx=10)

    instock_button = ctk.CTkButton(sidebar_frame, text="Stok Barang", command=lambda: adminstok.main_ui(app))
    instock_button.pack(pady=5, padx=10)

    transaksi_button = ctk.CTkButton(sidebar_frame, text="Transaksi", fg_color="green")
    transaksi_button.pack(pady=5, padx=10)

    users_button = ctk.CTkButton(sidebar_frame, text="Users", command=lambda:adminuser.setup_app(app), fg_color="purple")
    users_button.pack(pady=5, padx=10)

    # create the right content frame
    right_frame = ctk.CTkFrame(app, corner_radius=0)
    right_frame.pack(side="right", fill="both", expand=True)

    # create the top frame
    top_frame = ctk.CTkFrame(right_frame, corner_radius=0)
    top_frame.pack(fill="x", pady=10)

    # create the title
    title_label = ctk.CTkLabel(top_frame, text="Gudang Indiekost", font=("Arial", 18))
    title_label.pack(pady=10)

    # create the table frame
    table_frame = ctk.CTkFrame(right_frame, corner_radius=0)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # create a table using Treeview
    columns = ("No", "Jam Pemesanan", "Barang Pesanan", "Jumlah")

    table = ttk.Treeview(table_frame, columns=columns, show="headings")
    table.pack(fill="both", expand=True)

    # define column headings
    table.heading("No", text="No")
    table.heading("Jam Pemesanan", text="Jam Pemesanan")
    table.heading("Barang Pesanan", text="Barang Pesanan")
    table.heading("Jumlah", text="Jumlah")

    # define column widths
    table.column("No", width=50, anchor="center")
    table.column("Jam Pemesanan", width=150, anchor="center")
    table.column("Barang Pesanan", width=200, anchor="center")
    table.column("Jumlah", width=100, anchor="center")

    # Function to load data from spreadsheet
    def load_data(transaction_type):
        table.delete(*table.get_children())  # Clear existing table data
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        file_path = f"./report/{'sell' if transaction_type == 'Penjualan' else 'buy'}/{today}.xlsx"

        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            for _, row in df.iterrows():
                table.insert("", "end", values=(row["No"], row["Jam Pemesanan"], row["Barang Pesanan"], row["Jumlah"]))
            #print(f"Data loaded from {file_path}") #debug print
        else:
            messagebox.showinfo("Info", "Belum ada transaksi hari ini")

    # Create the bottom frame for options
    bottom_frame = ctk.CTkFrame(right_frame, corner_radius=0)
    bottom_frame.pack(fill="x", side="bottom", pady=10, padx=10)

    # Dropdown for transaction type
    tipe_transaksi = ["Penjualan", "Pembelian"]
    selected_transaction = ctk.StringVar(value="Penjualan")

    def on_transaction_change(choice):
        load_data(choice)

    export_button = ctk.CTkOptionMenu(bottom_frame, variable=selected_transaction, values=tipe_transaksi, command=on_transaction_change)
    export_button.pack(side="right", padx=10)

    # Load default data (Penjualan)
    load_data("Penjualan")

    # run the application
    app.mainloop()

if __name__ == "__main__":
    main(ctk.CTk())
