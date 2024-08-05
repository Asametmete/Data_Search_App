import mysql.connector
import tkinter as tk
from tkinter import ttk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cimbom.com123",
    database="testdb"
)
mycursor = mydb.cursor()

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Search app")
        self.root.geometry("700x600")
        self.root.resizable(0,0)

        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=8)  
        self.root.columnconfigure(2,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.rowconfigure(1,weight=1)
        self.root.rowconfigure(2,weight=1)

        
        self.btn = ttk.Button(self.root,text="BÜTÜN KULLANICI VERİLERİ İÇİN TIKLA",command=self.AllData)
        self.btn.grid(column=1,row=0,sticky="nswe")

        self.btn2 = ttk.Button(self.root,text="KULLANICI VERİLERİ İÇİN TIKLA",command=self.UsernameData)
        self.btn2.grid(column=1,row=1,sticky="nswe")

        self.btn3 = ttk.Button(self.root,text="FİLTRELEME VE ARAMA İÇİN TIKLA",command=self.filtreData)
        self.btn3.grid(column=1,row=2,sticky="nswe")

        self.database = Database(self)  #Database takes "self" for construction and our database object is ready 
    
    def AllData(self):
        self.rootAllData = tk.Tk()
        self.rootAllData.title("Bütün Kullanıcı Verileri")
        self.rootAllData.geometry("1200x600")
        self.rootAllData.resizable(0,0)

        self.rootAllData.columnconfigure(0,weight=1)
        self.rootAllData.columnconfigure(1,weight=8)  
        self.rootAllData.columnconfigure(2,weight=1)

        self.rootAllData.rowconfigure(0,weight=1)
        self.rootAllData.rowconfigure(1,weight=8)    

        self.lst = tk.Listbox(self.rootAllData,width=100,height=100)
        self.lst.grid(column=1,row=1)

        self.errLbl = tk.Label(self.rootAllData)
        self.errLbl.grid(column=1,row=0)

        self.database.AllDataDb(self.lst)    #We passed our variable to the Database class and the AllDataDb function works here

    def UsernameData(self):
        self.rootUsername = tk.Tk()
        self.rootUsername.title("Kullanıcı İsmine Göre Ara")
        self.rootUsername.geometry("1200x600")
        self.rootUsername.resizable(0,0)

        self.rootUsername.columnconfigure(0,weight=1)
        self.rootUsername.columnconfigure(1,weight=5)
        self.rootUsername.columnconfigure(2,weight=1)

        self.rootUsername.rowconfigure(0,weight=1)
        self.rootUsername.rowconfigure(1,weight=4)

        self.entry = tk.Entry(self.rootUsername,width=70)
        self.entry.grid(column=1,row=0)

        self.btn = tk.Button(self.rootUsername,text="Ara",command=self.database.userClsfct)   #It starts working when we click on it
        self.btn.grid(column=1,row=0,sticky="s")

        self.lbl = tk.Label(self.rootUsername,text="",background="gray",height=10,width=70)
        self.lbl.grid(column=1,row=1)

    def filtreData(self):
        self.rootFiltre = tk.Tk()
        self.rootFiltre.title("Filtreleyerek Ara")
        self.rootFiltre.geometry("1200x600")
        self.rootFiltre.resizable(0,0)

        
        self.rootFiltre.columnconfigure(0,weight=1)
        self.rootFiltre.columnconfigure(1,weight=5)
        self.rootFiltre.columnconfigure(2,weight=1)

        self.rootFiltre.rowconfigure(0,weight=1)
        self.rootFiltre.rowconfigure(1,weight=2)
        self.rootFiltre.rowconfigure(2,weight=2)
        self.rootFiltre.rowconfigure(3,weight=5)
        self.rootFiltre.rowconfigure(4,weight=1)

        self.errlbl2 = tk.Label(self.rootFiltre,text="",width=40)
        self.errlbl2.grid(column=1,row=4,sticky="n")

        #Combobox for position
        self.lblPosition = tk.Label(self.rootFiltre,text="Search for Position")
        self.lblPosition.grid(column=1,row=0,sticky="sw",padx=20)


        self.strPosition = tk.StringVar()  # This is takes the string values of the combobox when we need to what user selected then we can take this variable help
        self.positionCmb = ttk.Combobox(self.rootFiltre,textvariable=self.strPosition,state="readonly")
        self.positionCmb['values'] = ("Software Engineer","System Architect","Accountant","Junior Technical Author","Senior Javascript Developer","Integration Specialist","Sales Assistant","Javascript Developer",
                                    "Javascript Developer","Office Manager","Support Lead","Regional Director","Senior Marketing Designer","Marketing Designer","Chief Financial Officer (CFO)","Systems Administrator"
                                    "Personnel Lead","Development Lead","Chief Marketing Officer (CMO)","Pre-Sales Support","Chief Executive Officer (CEO)","Developer","Chief Operating Officer (COO)","Regional Marketing"
                                    "Technical Author","Team Leader","Post-Sales support","Secretary","Financial Controller","Director","Support Engineer","Data Coordinator","Junior Javascript Developer",
                                    "Customer Support")
        self.positionCmb.current()
        self.positionCmb.grid(column=1,row=1,sticky="nw")
        

        self.btn = tk.Button(self.rootFiltre,text="Ara",command=self.database.positionClsfct)
        self.btn.grid(column=1,row=1,sticky="nw",padx=150)


        #Combobox for Office
        self.lblOffice = tk.Label(self.rootFiltre,text="Search for Office")
        self.lblOffice.grid(column=1,row=0,sticky="sw",padx=320)

        self.strOffice = tk.StringVar()  
        self.officeCmb = ttk.Combobox(self.rootFiltre,textvariable=self.strOffice,state="readonly")
        self.officeCmb['values'] = ("Edinburgh","Tokyo","San Francisco","New York","London","London","Singapore")
        self.officeCmb.current()
        self.officeCmb.grid(column=1,row=1,sticky="nw",padx=300)
        
        self.btn2 = tk.Button(self.rootFiltre,text="Ara",command=self.database.officeClsfct)
        self.btn2.grid(column=1,row=1,sticky="nw",padx=450)


        #Entry for Age
        self.lblAge = tk.Label(self.rootFiltre,text="Search for Age")
        self.lblAge.grid(column=1,row=2,sticky="nw")

        self.AgeEntry =tk.Entry(self.rootFiltre,textvariable=int)
        self.AgeEntry.grid(column=1,row=2,sticky="w")

        self.AgeEntryBtn = tk.Button(self.rootFiltre,text="Ara",command=self.database.ageClsfct)
        self.AgeEntryBtn.grid(column=1,row=2,sticky="w",padx=130)




class Database:
    def __init__(self, ui):    #In this structure, we can use the Database class in another class and use the attributes and variables of this class in the methods of the Database class.
        self.ui = ui

    def AllDataDb(self,lst):
        try:
            mycursor.execute("SELECT * FROM dataprac2")
            myresult = mycursor.fetchall()
            for x in myresult:
                lst.insert(tk.END, x)
        except Exception:
            self.ui.errlbl.config(text="Someting went wrong...")

    def userClsfct(self):
        try:
            username_output = self.ui.entry.get()
            sql_formula = "SELECT * FROM dataprac2 WHERE name =%s"
            mycursor.execute(sql_formula , (username_output,))
            myresult = mycursor.fetchall()
            userResult = myresult[0][0]+"   "+myresult[0][1]+"   "+myresult[0][2]+"   "+str(myresult[0][3])+"   "+myresult[0][4]+"   "+myresult[0][5]
            self.ui.lbl.config(text=str(userResult))
        except Exception:
            self.ui.lbl.config(text="Username not found")

    def positionClsfct(self):
        try:
            position_output = self.ui.positionCmb.get()
            sql_formula = "SELECT * FROM dataprac2 WHERE position =%s"
            mycursor.execute(sql_formula , (position_output,))
            myresult = mycursor.fetchall()
            lst = tk.Listbox(self.ui.rootFiltre,width=100,height=20)        #Listbox had to created in this code line bcs evertime cliking button it will clean the listbox and give us new values
            for x in myresult:
                lst.insert(tk.END, x)
            lst.grid(column=1,row=3,sticky="s")
               
        except Exception:
            self.ui.errlbl2.config(text="Something went wrong...")
    
    def officeClsfct(self):
        try:
            office_output = self.ui.officeCmb.get()
            sql_formula = "SELECT * FROM dataprac2 WHERE office =%s"
            mycursor.execute(sql_formula , (office_output,))
            myresult = mycursor.fetchall()
            lst2 = tk.Listbox(self.ui.rootFiltre,width=100,height=20)       #Listbox had to created in this code line bcs evertime cliking button it will clean the listbox and give us new values
            for x in myresult:
                lst2.insert(tk.END, x)
            lst2.grid(column=1,row=3,sticky="s")
        except Exception:
            self.ui.errlbl2.config(text="Something went wrong...")     

    def ageClsfct(self):
        try:
            age_output = self.ui.AgeEntry.get()
            sql_formula = "SELECT * FROM dataprac2 WHERE age >= %s"
            mycursor.execute(sql_formula,(age_output,))
            myresult = mycursor.fetchall()
            lst3 = tk.Listbox(self.ui.rootFiltre,width=100,height=20)
            for x in myresult:
                lst3.insert(tk.END, x)
            lst3.grid(column=1,row=3,sticky="s")
        except Exception:
            self.ui.errlbl2.config(text="Something went wrong...")


        
 
class Main:
    def Exe():
        ui = UI()
        ui.root.mainloop()
Main.Exe()
mydb.commit()