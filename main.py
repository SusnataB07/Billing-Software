from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random, os, tempfile
from tkinter import messagebox
import subprocess
from time import strftime


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1536x793+0+0")
        self.root.title("Billing_Software")

        ###########################Variales##########################

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000, 9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        # Product Category Lists
        self.Category = ["Select Option", "Clothing", "Lifestyle", "Mobiles"]

        # Clothing
        self.SubCatClothing = ["Pant", "Shirt", "T_Shirt"]
        self.Pant = ["Levis", "Spykar", "Denim"]
        self.Price_Levis = 1500
        self.Price_Spykar = 1500
        self.Price_Denim = 1500

        self.Shirt = ["Peter England", "Louis Phillipe", "Park Avenue"]
        self.Price_PeterEngland = 1500
        self.Price_LouisPhillipe = 1500
        self.Price_ParkAvenue = 1500

        self.T_Shirt = ["Polo", "Roadstar", "Jack&Jones"]
        self.Price_Polo = 1200
        self.Price_Roadstar = 1300
        self.Price_JackJones = 1500

        # Lifestyle
        self.SubCatLifestyle = [
            "Bath Soap",
            "Face Creame",
            "Detergent",
            "Hair Oil",
            "Shampoo",
        ]

        self.Bath_soap = ["LifeBuy", "Lux", "Santoor", "Pearl"]
        self.price_life = 20
        self.price_lux = 20
        self.price_santoor = 20
        self.price_pearl = 30

        self.Face_creame = ["Fair&Lovely", "Ponds", "Olay", "Garnier"]
        self.price_fair = 20
        self.price_ponds = 20
        self.price_olay = 20
        self.price_garnier = 30

        self.Detergent = ["Ghadi", "SurfExcel", "Tide", "Ariel"]
        self.price_Ghadi = 20
        self.price_SurfExcel = 20
        self.price_Tide = 20
        self.price_Ariel = 30

        self.Hair_oil = ["Parachute", "Jashmin", "Bajaj"]
        self.price_para = 25
        self.price_jashmin = 22
        self.price_bajaj = 30

        self.Shampoo = ["Clinic Plus", "Head&Solder", "Vatika"]
        self.price_ClinicPlus = 25
        self.price_HeadSolder = 22
        self.price_Vatika = 30

        # Mobile
        self.SubCatMobiles = ["IPhone", "Samsung", "Oppo", "One+", "Vivo"]

        self.IPhone = ["IPhone 16", "IPhone 15", "IPhone 14"]
        self.price_iphone16 = 120000
        self.price_iphone15 = 100000
        self.price_iphone14 = 80000

        self.Samsung = ["Galaxy S24", "Galaxy S23", "Galaxy A55"]
        self.price_s24 = 90000
        self.price_s23 = 75000
        self.price_a55 = 35000

        self.Oppo = ["Oppo Find X7", "Oppo Reno 11", "Oppo A78"]
        self.price_findx7 = 70000
        self.price_reno11 = 40000
        self.price_a78 = 20000

        self.Oneplus = ["OnePlus 12", "OnePlus 11", "OnePlus Nord 3"]
        self.price_oneplus12 = 60000
        self.price_oneplus11 = 50000
        self.price_nord3 = 30000

        self.Vivo = ["Vivo X100", "Vivo V30", "Vivo Y200"]
        self.price_x100 = 65000
        self.price_v30 = 30000
        self.price_y200 = 20000

        # Top image
        img = Image.open("image/images0.jpeg")  # import image to screen
        img = img.resize((1536, 100))  # (width,height)
        self.photoimg = ImageTk.PhotoImage(img)  # (PhotoImage-> Convert photo to image)

        lebel_img = Label(self.root, image=self.photoimg)
        lebel_img.place(x=0, y=0, width=1536, height=100)

        lebel_title = Label(
            self.root,
            text="Billing Software Using Python",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        lebel_title.place(x=0, y=100, width=1536, height=60)

        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(
            lebel_title, font=("times new roman", 16, "bold"), bg="white", fg="blue"
        )
        lbl.place(x=1, y=0, width=120, height=45)
        time()

        Main_Frame = Frame(self.root, bd="5", relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=160, width=1536, height=793)

        # Customer Frame
        Cust_Frame = LabelFrame(
            Main_Frame,
            text="Customer",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
        )
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        # Mobile No.
        self.lebel_mob = Label(
            Cust_Frame,
            text="Mobile No.",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        self.lebel_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(
            Cust_Frame, textvariable=self.c_phone, font=("arial", 10, "bold"), width=24
        )
        self.entry_mob.grid(row=0, column=1)

        # Customer Name
        self.lebel_CustName = Label(
            Cust_Frame,
            text="Customer Name",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_CustName.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.txt_CustName = ttk.Entry(
            Cust_Frame, textvariable=self.c_name, font=("arial", 10, "bold"), width=24
        )
        self.txt_CustName.grid(row=1, column=1, stick=W, padx=5, pady=2)

        # Email
        self.lebel_Email = Label(
            Cust_Frame, text="Email", font=("arial", 12, "bold"), bg="white", bd=4
        )
        self.lebel_Email.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txt_Email = ttk.Entry(
            Cust_Frame, textvariable=self.c_email, font=("arial", 10, "bold"), width=24
        )
        self.txt_Email.grid(row=2, column=1, stick=W, padx=5, pady=2)

        # Product LabelFrame
        Prod_Frame = LabelFrame(
            Main_Frame,
            text="Product",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
        )
        Prod_Frame.place(x=370, y=5, width=750, height=140)

        # Category
        self.lebel_Category = Label(
            Prod_Frame,
            text="Select Category",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_Category.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(
            Prod_Frame,
            value=self.Category,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        # Subcategory
        self.lebel_SubCategory = Label(
            Prod_Frame,
            text="Subcategory",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_SubCategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.Combo_SubCategory = ttk.Combobox(
            Prod_Frame,
            value=[""],
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.Combo_SubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>", self.Product_Add)

        # Product Name
        self.lebel_ProdName = Label(
            Prod_Frame,
            text="Product Name",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_ProdName.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.Combo_ProdName = ttk.Combobox(
            Prod_Frame,
            textvariable=self.product,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.Combo_ProdName.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.Combo_ProdName.bind("<<ComboboxSelected>>", self.Price)

        # Price
        self.lebel_Price = Label(
            Prod_Frame,
            text="Price",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_Price.grid(row=0, column=2, stick=W, padx=5, pady=2)

        self.Combo_Price = ttk.Combobox(
            Prod_Frame,
            textvariable=self.prices,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.Combo_Price.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Quantity(Qty)
        self.lebel_Qty = Label(
            Prod_Frame,
            text="Quantity",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_Qty.grid(row=1, column=2, stick=W, padx=5, pady=2)

        self.Combo_Qty = ttk.Combobox(
            Prod_Frame,
            textvariable=self.qty,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
            values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )
        self.Combo_Qty.current(0)
        self.Combo_Qty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Middle Frame
        Middle_Frame = Frame(Main_Frame, bd=10)
        Middle_Frame.place(x=10, y=155, width=1110, height=330)

        # image 1
        img1 = Image.open("image/image3.jpg")  # import image to screen
        img1 = img1.resize((545, 310))  # (width,height)
        self.photoimg1 = ImageTk.PhotoImage(
            img1
        )  # (PhotoImage-> Convert photo to image)

        lebel_img1 = Label(Middle_Frame, image=self.photoimg1)
        lebel_img1.place(x=0, y=0, width=540, height=310)

        # image 2
        img2 = Image.open("image/image2.jpeg")  # import image to screen
        img2 = img2.resize((545, 310))  # (width,height)
        self.photoimg2 = ImageTk.PhotoImage(
            img2
        )  # (PhotoImage-> Convert photo to image)

        lebel_img2 = Label(Middle_Frame, image=self.photoimg2)
        lebel_img2.place(x=550, y=0, width=540, height=310)

        # Search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=1130, y=5, width=390, height=35)

        self.lebel_SearchBill = Label(
            Search_Frame,
            text="Bill number",
            font=("arial", 12, "bold"),
            bg="red",
            fg="white",
        )
        self.lebel_SearchBill.grid(row=0, column=0, stick=W, padx=2, pady=3)

        self.EntrySearch = ttk.Entry(
            Search_Frame,
            textvariable=self.search_bill,
            font=("arial", 12, "bold"),
            width=24,
        )
        self.EntrySearch.grid(row=0, column=1, sticky=W, padx=2, pady=2)

        self.Search_Button = Button(
            Search_Frame,
            command=self.find_bill,
            text="Search",
            font=("arial", 11, "bold"),
            bg="orange",
            fg="white",
            cursor="hand2",
        )
        self.Search_Button.grid(row=0, column=2)

        # RightFrame Bill Area
        RightLabelframe = LabelFrame(
            Main_Frame,
            text="Bill Area",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
        )
        RightLabelframe.place(x=1130, y=45, width=390, height=440)

        scroll_y = Scrollbar(RightLabelframe, orient=VERTICAL)
        self.textarea = Text(
            RightLabelframe,
            yscrollcommand=scroll_y.set,
            bg="white",
            fg="blue",
            font=("times new roman", 12, "bold"),
        )
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter LabelFrame
        Bottom_Frame = LabelFrame(
            Main_Frame,
            text="Bill Counter",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
        )
        Bottom_Frame.place(x=10, y=494, width=1510, height=125)

        # SubTotal
        self.lebel_SubTotal = Label(
            Bottom_Frame,
            text="Sub Total",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_SubTotal.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.EntySubTotal = ttk.Entry(
            Bottom_Frame,
            textvariable=self.sub_total,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.EntySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # Tax
        self.lebel_Tax = Label(
            Bottom_Frame,
            text="Tax",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_Tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.text_Tax = ttk.Entry(
            Bottom_Frame,
            textvariable=self.tax_input,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.text_Tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        # TotalAmount
        self.lebel_TotalAmount = Label(
            Bottom_Frame,
            text="Total Amount",
            font=("arial", 12, "bold"),
            bg="white",
            bd=4,
        )
        self.lebel_TotalAmount.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txt_TotalAmount = ttk.Entry(
            Bottom_Frame,
            textvariable=self.total,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.txt_TotalAmount.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Button Frame
        Btn_Frame = Frame(Bottom_Frame, bd=2, bg="white")
        Btn_Frame.place(x=360, y=13)

        self.btnAddToCart = Button(
            Btn_Frame,
            command=self.AddItem,
            height=2,
            text="Add To Cart",
            font=("arial", 15, "bold"),
            bg="orange",
            fg="white",
            width=14,
            cursor="hand2",
        )
        self.btnAddToCart.grid(row=0, column=0, padx=5)

        self.generatebill = Button(
            Btn_Frame,
            command=self.Gen_Bill,
            height=2,
            text="Generate Bill",
            font=("arial", 15, "bold"),
            bg="orange",
            fg="white",
            width=14,
            cursor="hand2",
        )
        self.generatebill.grid(row=0, column=1, padx=5)

        self.savebill = Button(
            Btn_Frame,
            command=self.Save_Bill,
            height=2,
            text="Save Bill",
            font=("arial", 15, "bold"),
            bg="orange",
            fg="white",
            width=14,
            cursor="hand2",
        )
        self.savebill.grid(row=0, column=2, padx=5)

        self.Btnprint = Button(
            Btn_Frame,
            command=self.iPrint,
            height=2,
            text="Print",
            font=("arial", 15, "bold"),
            bg="orange",
            fg="white",
            width=14,
            cursor="hand2",
        )
        self.Btnprint.grid(row=0, column=3, padx=5)

        self.clear = Button(
            Btn_Frame,
            command=self.Clear_All,
            height=2,
            text="Clear",
            font=("arial", 15, "bold"),
            bg="orange",
            fg="white",
            width=14,
            cursor="hand2",
        )
        self.clear.grid(row=0, column=4, padx=5)

        self.exit = Button(
            Btn_Frame,
            command=self.root.destroy,
            height=2,
            text="Exit",
            font=("arial", 15, "bold"),
            bg="orange",
            fg="white",
            width=14,
            cursor="hand2",
        )
        self.exit.grid(row=0, column=5, padx=5)

        self.welcome()

        self.l = []

    # ====================Funtion Declaration==============

    def AddItem(self):
        Tax = 1
        qty = int(self.qty.get()) if self.qty.get() else 0
        price = float(self.prices.get()) if self.prices.get() else 0
        self.m = qty * price
        self.l.append(self.m)

        if self.product.get() == "":
            messagebox.showerror("Error", "Please Select the Product Name")
        else:
            self.textarea.insert(END, f"\n {self.product.get()}\t\t{qty}\t\t{self.m}")
            self.sub_total.set(f"Rs.{sum(self.l):.2f}")
            self.tax_input.set(f"Rs.{((sum(self.l) * Tax) / 100):.2f}")
            self.total.set(f"Rs.{sum(self.l) + ((sum(self.l) * Tax) / 100):.2f}")

    def Gen_Bill(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Please Add To Cart Products")
        else:
            text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, "\n========================================")
            self.textarea.insert(END, f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n========================================")

    def Save_Bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill ?")
        if op > 0:
            self.bill_data = self.textarea.get(1.0, END)
            with open("bills/" + str(self.bill_no.get()) + ".txt", "w") as f1:
                f1.write(self.bill_data)
                op = messagebox.showinfo(
                    "Saved", f"Bill No.{self.bill_no.get()} Saved Succesfully"
                )

    def iPrint(self):
        q = self.textarea.get(1.0, "end-1c")
        filename = tempfile.mktemp(".txt")
        open(filename, "w").write(q)
        subprocess.run(["notepad.exe", "/p", filename])

    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split(".")[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                found = "yes"
        if found == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def Clear_All(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l = [0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()

    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\tWelcome To Magic Mall")
        self.textarea.insert(END, f"\n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer name: {self.c_name.get()}")
        self.textarea.insert(END, f"\n Mobile number: {self.c_phone.get()}")
        self.textarea.insert(END, f"\n Email: {self.c_email.get()}")

        self.textarea.insert(END, f"\n========================================")
        self.textarea.insert(END, f"\n Products\t\t\tQTY\tPrice")
        self.textarea.insert(END, f"\n========================================\n")

    def Categories(self, events=""):
        if self.Combo_Category.get() == "Clothing":
            self.Combo_SubCategory.config(value=self.SubCatClothing)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "Lifestyle":
            self.Combo_SubCategory.config(value=self.SubCatLifestyle)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "Mobiles":
            self.Combo_SubCategory.config(value=self.SubCatMobiles)
            self.Combo_SubCategory.current(0)

    def Product_Add(self, event=""):
        if self.Combo_SubCategory.get() == "Pant":
            self.Combo_ProdName.config(value=self.Pant)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Shirt":
            self.Combo_ProdName.config(value=self.Shirt)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "T_Shirt":
            self.Combo_ProdName.config(value=self.T_Shirt)
            self.Combo_ProdName.current(0)

        # Lifestyle
        if self.Combo_SubCategory.get() == "Bath Soap":
            self.Combo_ProdName.config(value=self.Bath_soap)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Face Creame":
            self.Combo_ProdName.config(value=self.Face_creame)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Detergent":
            self.Combo_ProdName.config(value=self.Detergent)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Hair Oil":
            self.Combo_ProdName.config(value=self.Hair_oil)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Shampoo":
            self.Combo_ProdName.config(value=self.Shampoo)
            self.Combo_ProdName.current(0)

        # Mobiles
        if self.Combo_SubCategory.get() == "IPhone":
            self.Combo_ProdName.config(value=self.IPhone)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Samsung":
            self.Combo_ProdName.config(value=self.Samsung)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Oppo":
            self.Combo_ProdName.config(value=self.Oppo)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "One+":
            self.Combo_ProdName.config(value=self.Oneplus)
            self.Combo_ProdName.current(0)

        if self.Combo_SubCategory.get() == "Vivo":
            self.Combo_ProdName.config(value=self.Vivo)
            self.Combo_ProdName.current(0)

    def Price(self, event=""):
        # Pant
        if self.Combo_ProdName.get() == "Levis":
            self.Combo_Price.config(value=self.Price_Levis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Spykar":
            self.Combo_Price.config(value=self.Price_Spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Denim":
            self.Combo_Price.config(value=self.Price_Denim)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Shirt
        if self.Combo_ProdName.get() == "Peter England":
            self.Combo_Price.config(value=self.Price_PeterEngland)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Louis Phillipe":
            self.Combo_Price.config(value=self.Price_LouisPhillipe)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Park Avenue":
            self.Combo_Price.config(value=self.Price_ParkAvenue)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # T-Shirt
        if self.Combo_ProdName.get() == "Polo":
            self.Combo_Price.config(value=self.Price_Polo)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Roadstar":
            self.Combo_Price.config(value=self.Price_Roadstar)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Jack&Jones":
            self.Combo_Price.config(value=self.Price_JackJones)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # ================= Lifestyle =================
        # Bath Soap
        if self.Combo_ProdName.get() == "LifeBuy":
            self.Combo_Price.config(value=self.price_life)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Lux":
            self.Combo_Price.config(value=self.price_lux)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Santoor":
            self.Combo_Price.config(value=self.price_santoor)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Pearl":
            self.Combo_Price.config(value=self.price_pearl)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Face Creame
        if self.Combo_ProdName.get() == "Fair&Lovely":
            self.Combo_Price.config(value=self.price_fair)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Ponds":
            self.Combo_Price.config(value=self.price_ponds)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Olay":
            self.Combo_Price.config(value=self.price_olay)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Garnier":
            self.Combo_Price.config(value=self.price_garnier)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Detergent
        if self.Combo_ProdName.get() == "Ghadi":
            self.Combo_Price.config(value=self.price_Ghadi)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "SurfExcel":
            self.Combo_Price.config(value=self.price_SurfExcel)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Tide":
            self.Combo_Price.config(value=self.price_Tide)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Ariel":
            self.Combo_Price.config(value=self.price_Ariel)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Hair Oil
        if self.Combo_ProdName.get() == "Parachute":
            self.Combo_Price.config(value=self.price_para)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Jashmin":
            self.Combo_Price.config(value=self.price_jashmin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Bajaj":
            self.Combo_Price.config(value=self.price_bajaj)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Shampoo
        if self.Combo_ProdName.get() == "Clinic Plus":
            self.Combo_Price.config(value=self.price_ClinicPlus)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Head&Solder":
            self.Combo_Price.config(value=self.price_HeadSolder)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Vatika":
            self.Combo_Price.config(value=self.price_Vatika)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # ================= Mobiles =================
        # IPhone
        if self.Combo_ProdName.get() == "IPhone 16":
            self.Combo_Price.config(value=self.price_iphone16)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "IPhone 15":
            self.Combo_Price.config(value=self.price_iphone15)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "IPhone 14":
            self.Combo_Price.config(value=self.price_iphone14)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Samsung
        if self.Combo_ProdName.get() == "Galaxy S24":
            self.Combo_Price.config(value=self.price_s24)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Galaxy S23":
            self.Combo_Price.config(value=self.price_s23)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Galaxy A55":
            self.Combo_Price.config(value=self.price_a55)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Oppo
        if self.Combo_ProdName.get() == "Oppo Find X7":
            self.Combo_Price.config(value=self.price_findx7)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Oppo Reno 11":
            self.Combo_Price.config(value=self.price_reno11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Oppo A78":
            self.Combo_Price.config(value=self.price_a78)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # OnePlus
        if self.Combo_ProdName.get() == "OnePlus 12":
            self.Combo_Price.config(value=self.price_oneplus12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "OnePlus 11":
            self.Combo_Price.config(value=self.price_oneplus11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "OnePlus Nord 3":
            self.Combo_Price.config(value=self.price_nord3)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # Vivo
        if self.Combo_ProdName.get() == "Vivo X100":
            self.Combo_Price.config(value=self.price_x100)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Vivo V30":
            self.Combo_Price.config(value=self.price_v30)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProdName.get() == "Vivo Y200":
            self.Combo_Price.config(value=self.price_y200)
            self.Combo_Price.current(0)
            self.qty.set(1)


if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
