from customtkinter import *
from tkinter import ttk, filedialog
import csv

set_appearance_mode("System")
set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green", "dark-green", "light-blue", "dark-gray", "gray"

# create the main window
app = CTk()
app.geometry("700x500")
app.title("Inventory")

# create the sidebar
sidebar_frame = CTkFrame(app, width=140, corner_radius=0)
sidebar_frame.pack(side="left", fill="y")

# create the sidebar buttons
dashboard_button = CTkButton(sidebar_frame, text="Dashboard", command=lambda: print("Dashboard Button clicked"))
dashboard_button.pack(pady=5, padx=10)

instock_button = CTkButton(sidebar_frame, text="In Stock", command=lambda: print("In Stock Button clicked"))
instock_button.pack(pady=5, padx=10)

products_button = CTkButton(sidebar_frame, text="Products", command=lambda: print("Products Button clicked"))
products_button.pack(pady=5, padx=10)

sales_button = CTkButton(sidebar_frame, text="Sales", command=lambda: print("Sales Button clicked"))
sales_button.pack(pady=5, padx=10)

orders_button = CTkButton(sidebar_frame, text="Orders", command=lambda: print("Orders Button clicked"))
orders_button.pack(pady=5, padx=10)

users_button = CTkButton(sidebar_frame, text="Users", command=lambda: print("Users Button clicked"))
users_button.pack(pady=5, padx=10)

# create the right content frame
right_frame = CTkFrame(app, corner_radius=0)
right_frame.pack(side="right", fill="both", expand=True)

# create the top frame
top_frame = CTkFrame(right_frame, corner_radius=0)
top_frame.pack(fill="x", pady=10)

# create the title
title_label = CTkLabel(top_frame, text="Inventory Table", font=("Arial", 18))
title_label.pack(pady=10)

# create the table frame
table_frame = CTkFrame(right_frame, corner_radius=0)
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

# create a table using Treeview
columns = ("No", "Tgl Pemesanan", "Pesanan", "Jumlah", "Harga", "Total")

table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
table.pack(fill="both", expand=True)

# define column headings
table.heading("No", text="No")
table.heading("Tgl Pemesanan", text="Tgl Pemesanan")
table.heading("Pesanan", text="Pesanan")
table.heading("Jumlah", text="Jumlah")
table.heading("Harga", text="Harga")
table.heading("Total", text="Total")

# define column widths
table.column("No", width=50, anchor="center")
table.column("Tgl Pemesanan", width=150, anchor="center")
table.column("Pesanan", width=100, anchor="center")
table.column("Jumlah", width=100, anchor="center")
table.column("Harga", width=100, anchor="center")
table.column("Total", width=100, anchor="center")

# insert sample data
sample_data = [
    (1, "1/1/2024", "Nasi Goreng", "10", 50, 500),
    (2, "2/1/2024", "Mie Goreng", "5", 40, 200),
    (3, "3/1/2024", "Soto Ayam", "8", 60, 480),
    (4, "4/1/2024", "Bakso", "15", 30, 450),
    (5, "5/1/2024", "Ayam Geprek", "12", 35, 420)
]

for row in sample_data:
    table.insert("", "end", values=row)

# Function to export table data to CSV
def export_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # write the column headings
            writer.writerow(columns)
            # write the data rows
            for item in table.get_children():
                writer.writerow(table.item(item, "values"))
        print(f"Data exported to {file_path}")

# Function to add new data
def add_row():
    # Add a new row (for simplicity, this is hardcoded)
    new_row = (len(table.get_children()) + 1, "6/1/2024", "Es Teh", "20", 10, 200)
    table.insert("", "end", values=new_row)
    print("New row added!")

# Create the bottom frame for buttons
bottom_frame = CTkFrame(right_frame, corner_radius=0)
bottom_frame.pack(fill="x", side="bottom", pady=10, padx=10)

# Create Export button
export_button = CTkButton(bottom_frame, text="Export", command=export_to_csv)
export_button.pack(side="right", padx=10)

# Create Plus button
plus_button = CTkButton(bottom_frame, text="+", width=40, height=40, font=("Arial", 18), command=add_row)
plus_button.pack(side="right")

# run the application
app.mainloop()
