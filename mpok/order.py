import customtkinter as ctk
import tkinter
from PIL import Image
import mpok.dashboard as adminlogin
import mpok.stok as adminstok
import mpok.transaksi as admintransaksi
import mpok.user as adminuser

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

def lihat_order(app):
# App Windows GUI
    for widget in app.winfo_children():
        widget.destroy()

    sidebar_frame = ctk.CTkFrame(master=app, fg_color="#2A8C55",  width=176, height=650, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    ctk.CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

    ctk.CTkButton(master=sidebar_frame, image=analytics_img, text="Dashboard", command=lambda: adminlogin.main(app), fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

    ctk.CTkButton(master=sidebar_frame, image=package_img, text="Pesanan", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    ctk.CTkButton(master=sidebar_frame, image=list_img, text="Stock", command=lambda: adminstok.main_ui(app), fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    ctk.CTkButton(master=sidebar_frame, image=returns_img, text="Transaksi", command=lambda: admintransaksi.main(app), fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    ctk.CTkButton(master=sidebar_frame, image=person_img, text="User", command=lambda: adminuser.setup_app(app), fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

    main_view = ctk.CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="left")

    ctk.CTkLabel(master=main_view, text="Create Order", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29,0), padx=27)
    ctk.CTkLabel(master=main_view, text="Item Name", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25,0), padx=27)
    ctk.CTkEntry(master=main_view, fg_color="#F0F0F0", border_width=0).pack(fill="x", pady=(12,0), padx=27, ipady=10)

    grid = ctk.CTkFrame(master=main_view, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31,0))

    ctk.CTkLabel(master=grid, text="Customer", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=0, column=0, sticky="w")
    ctk.CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=0, ipady=10)

    ctk.CTkLabel(master=grid, text="Address", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
    ctk.CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=1, ipady=10, padx=(24,0))

    ctk.CTkLabel(master=grid, text="Status", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=2, column=0, sticky="w", pady=(38, 0))

    status_var = tkinter.IntVar(value=0)

    ctk.CTkRadioButton(master=grid, variable=status_var, value=0, text="Confirmed", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=3, column=0, sticky="w", pady=(16,0))
    ctk.CTkRadioButton(master=grid, variable=status_var, value=1,text="Pending", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=4, column=0, sticky="w", pady=(16,0))
    ctk.CTkRadioButton(master=grid, variable=status_var, value=2,text="Cancelled", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=5, column=0, sticky="w", pady=(16,0))

    ctk.CTkLabel(master=grid, text="Quantity", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=6, column=0, sticky="w", pady=(42, 0))

    quantity_frame = ctk.CTkFrame(master=grid, fg_color="transparent")
    quantity_frame.grid(row=7, column=0, pady=(21,0), sticky="w")
    ctk.CTkButton(master=quantity_frame, text="-", width=25, fg_color="#2A8C55", hover_color="#207244", font=("Arial Black", 16)).pack(side="left", anchor="w")
    ctk.CTkLabel(master=quantity_frame, text="01", text_color="#2A8C55", font=("Arial Black", 16)).pack(side="left", anchor="w", padx=10)
    ctk.CTkButton(master=quantity_frame, text="+", width=25,  fg_color="#2A8C55",hover_color="#207244", font=("Arial Black", 16)).pack(side="left", anchor="w")

    ctk.CTkLabel(master=grid, text="Description", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=2, column=1, sticky="w", pady=(42, 0), padx=(25,0))

    ctk.CTkTextbox(master=grid, fg_color="#F0F0F0", width=300, corner_radius=8).grid(row=3, column=1, rowspan=5, sticky="w", pady=(16, 0), padx=(25,0), ipady=10)

    actions= ctk.CTkFrame(master=main_view, fg_color="transparent")
    actions.pack(fill="both")

    ctk.CTkButton(master=actions, text="Back", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#2A8C55", hover_color="#eee", border_width=2, text_color="#2A8C55").pack(side="left", anchor="sw", pady=(30,0), padx=(27,24))
    ctk.CTkButton(master=actions, text="Create", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff").pack(side = "left", anchor="se", pady=(30,0), padx=(0,27))

    app.mainloop()