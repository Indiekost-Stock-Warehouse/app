import customtkinter as ctk
from CTkTable import CTkTable
from PIL import Image
import mpok.user as userui
from mpok.stok import main as fungsi

#Images
logo_img_data = Image.open("./Asset/Image/logo.png")
logo_img = ctk.CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

analytics_img_data = Image.open("./Asset/Image/analytics_icon.png")
analytics_img = ctk.CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)

package_img_data = Image.open("./Asset/Image/package_icon.png")
package_img = ctk.CTkImage(dark_image=package_img_data, light_image=package_img_data)

list_img_data = Image.open("./Asset/Image/list_icon.png")
list_img = ctk.CTkImage(dark_image=list_img_data, light_image=list_img_data)

returns_img_data = Image.open("./Asset/Image/returns_icon.png")
returns_img = ctk.CTkImage(dark_image=returns_img_data, light_image=returns_img_data)

settings_img_data = Image.open("./Asset/Image/settings_icon.png")
settings_img = ctk.CTkImage(dark_image=settings_img_data, light_image=settings_img_data)

person_img_data = Image.open("./Asset/Image/person_icon.png")
person_img = ctk.CTkImage(dark_image=person_img_data, light_image=person_img_data)

logitics_img_data = Image.open("./Asset/Image/logistics_icon.png")
logistics_img = ctk.CTkImage(light_image=logitics_img_data, dark_image=logitics_img_data, size=(43, 43))

delivered_img_data = Image.open("./Asset/Image/delivered_icon.png")
delivered_img = ctk.CTkImage(light_image=delivered_img_data, dark_image=delivered_img_data, size=(43, 43))

shipping_img_data = Image.open("./Asset/Image/shipping_icon.png")
shipping_img = ctk.CTkImage(light_image=shipping_img_data, dark_image=shipping_img_data, size=(43, 43))

# App Windows GUI
def show_dashboard(app):
    # Clear previous widgets
    for widget in app.winfo_children():
        widget.destroy()

    sidebar_frame = ctk.CTkFrame(master=app, fg_color="#2A8C55",  width=176, height=650, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    ctk.CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

    ctk.CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", command=lambda: fungsi(app), fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

    ctk.CTkButton(master=sidebar_frame, image=package_img, text="Orders", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    ctk.CTkButton(master=sidebar_frame, image=list_img, text="Orders", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    ctk.CTkButton(master=sidebar_frame, image=returns_img, text="Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    ctk.CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    ctk.CTkButton(master=sidebar_frame, image=person_img, text="Account", command=lambda: userui.setup_app(app), fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

    main_view = ctk.CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="left")

    title_frame = ctk.CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    ctk.CTkLabel(master=title_frame, text="Orders", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", side="left")

    ctk.CTkButton(master=title_frame, text="+ New Order",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244").pack(anchor="ne", side="right")

    metrics_frame = ctk.CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

    orders_metric = ctk.CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")

    ctk.CTkLabel(master=orders_metric, image=logistics_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    ctk.CTkLabel(master=orders_metric, text="Orders", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    ctk.CTkLabel(master=orders_metric, text="123", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    shipped_metric = ctk.CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
    shipped_metric.grid_propagate(0)
    shipped_metric.pack(side="left",expand=True, anchor="center")

    ctk.CTkLabel(master=shipped_metric, image=shipping_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    ctk.CTkLabel(master=shipped_metric, text="Shipping", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    ctk.CTkLabel(master=shipped_metric, text="91", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    delivered_metric = ctk.CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
    delivered_metric.grid_propagate(0)
    delivered_metric.pack(side="right",)

    ctk.CTkLabel(master=delivered_metric, image=delivered_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    ctk.CTkLabel(master=delivered_metric, text="Delivered", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    ctk.CTkLabel(master=delivered_metric, text="23", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    search_container = ctk.CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(45, 0), padx=27)

    ctk.CTkEntry(master=search_container, width=305, placeholder_text="Search Order", border_color="#2A8C55", border_width=2).pack(side="left", padx=(13, 0), pady=15)

    ctk.CTkComboBox(master=search_container, width=125, values=["Date", "Most Recent Order", "Least Recent Order"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
    ctk.CTkComboBox(master=search_container, width=125, values=["Status", "Processing", "Confirmed", "Packing", "Shipping", "Delivered", "Cancelled"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

    table_data = [
        ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
        ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
        ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
        ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
        ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
        ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
        ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
        ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
        ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
        ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
        ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
        ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
        ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
        ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
        ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
        ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
        ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
        ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
        ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10']
    ]

    table_frame = ctk.CTkScrollableFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

    app.mainloop()