from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 
con = sqlite3.connect('HOSPITAL.db')
cur = con.cursor()



class Hospital:

    #Functions
    def addPrescription(self):        
        try:
            if self.ref.get() =="" or self.doctor.get() =="":
                messagebox.showerror("ERROR",'PLEASE ENTER ALL REQUIRED FIELDS')
            else:
                con = sqlite3.connect('HOSPITAL.db')
                cur = con.cursor()
                cur.execute('INSERT INTO HOSPITAL VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(
                self.nameOftablets.get(),
                self.ref.get(),
                self.Dose.get(), 
                self.Numberoftablets.get(),
                self.doctor.get(), 
                self.Issuedate.get(),
                self.ExpDate.get(), 
                self.DailyDose.get(), 
                self.StorageAdvice.get(),
                self.patientId.get(), 
                self.PatientName.get(),
                self.DateOfBirth.get(), 
                self.PatientAddress.get()
                )   
                )
                con.commit()
                self.fetchData()
                con.close()
                messagebox.showinfo('SUCCESS',"PATIENT DETAILS HAVE BEEN ADDED")
        except:
            messagebox.showerror('ERROR',"CANNOT ENTER ALREADY EXISTING REFERENCE NUMBER")

    def fetchData(self):
        con = sqlite3.connect('HOSPITAL.db')
        cur =con.cursor()
        cur.execute("SELECT * FROM HOSPITAL")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", "end", values=i)
        con.commit()
        con.close()

    def myCursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.nameOftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Numberoftablets.set(row[3])
        self.doctor.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        # self.sideEffect.set(row[8])
        # self.FurtherInformation.set(row[9])
        self.StorageAdvice.set(row[8])
        # self.bloodPressure.set(row[11])
        # self.HowToUseMedication.set(row[12])
        # self.PatientId.set(row[13])
        self.patientId.set(row[9])
        self.PatientName.set(row[10]) 
        self.DateOfBirth.set(row[11]) 
        self.PatientAddress.set(row[12])


    def updateData(self):
        up = messagebox.askquestion("UPDATE","Are you sure you want to updateData?")
        if int(up=='yes'):
            if self.ref.get() == "" or self.doctor.get() == "":
                messagebox.showerror("ERROR","Enter all required fields")
            else:
                con = sqlite3.connect('HOSPITAL.db')
                cur =con.cursor()
                cur.execute('UPDATE HOSPITAL SET nameOfTablets =?,dose = ?,numberOfTablets = ?,doctor  = ?,issueDate = ?,expDate = ?,dailyDose = ?,storage = ?,patientId = ?,patientName = ?,DOB = ?, patientAddress = ? WHERE referenceNo = ?',(
                self.nameOftablets.get(),
                self.Dose.get(),
                self.Numberoftablets.get(),
                self.doctor.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.patientId.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get(),
                ))
            con.commit()
            self.fetchData()
            con.close()
            messagebox.showinfo('UPDATE','FIELDS SUCCESSFULLY UPDATED')
        else:
            return    

    def delete(self):
        con = sqlite3.connect('HOSPITAL.db')
        cur =con.cursor()
        cur.execute('DELETE FROM HOSPITAL WHERE referenceNo = ?',(self.ref.get(),))
        con.commit()
        messagebox.showinfo("DELETE","DELETED SUCCESSFULLY")
        self.fetch_data()
        con.close()

    def showPrescription(self):
        self.txtPrescription.insert("end","Name of Tablets:\t\t\t"+ self.nameOftablets.get()+"\n")
        self.txtPrescription.insert("end","Reference No.:\t\t\t"+ self.ref.get()+"\n")
        self.txtPrescription.insert("end","Dose:\t\t\t"+ self.Dose.get()+"\n")
        self.txtPrescription.insert("end","Number of Tablets:\t\t\t"+ self.Numberoftablets.get()+"\n")
        self.txtPrescription.insert("end","Consulted by Doctor:\t\t\t"+ self.doctor.get()+"\n")
        self.txtPrescription.insert("end","Issue Date:\t\t\t"+ self.Issuedate.get()+"\n")
        self.txtPrescription.insert("end","Exp Date:\t\t\t"+ self.ExpDate.get()+"\n")
        self.txtPrescription.insert("end","Daily Dose:\t\t\t"+ self.DailyDose.get()+"\n")
        #self.txtPrescription.insert("end","Side Effect:\t\t\t"+ self.sideEffect.get()+"\n")
        #self.txtPrescription.insert("end","Further Information:\t\t\t"+ self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert("end","Storage Advice:\t\t\t"+ self.StorageAdvice.get()+"\n")
        #self.txtPrescription.insert("end","Blood Pressure:\t\t\t"+ self.bloodPressure.get()+"\n")
        #self.txtPrescription.insert("end","Patient ID:\t\t\t"+ self.PatientId.get()+"\n")
        self.txtPrescription.insert("end","Patient ID:\t\t\t"+ self.patientId.get()+"\n")
        self.txtPrescription.insert("end","Patient Name:\t\t\t"+ self.PatientName.get()+"\n")
        self.txtPrescription.insert("end","Date of Birth:\t\t\t"+ self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert("end","Patient Address:\t\t\t"+ self.PatientAddress.get()+"\n")

    def clearAll(self):
        self.nameOftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.doctor.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.patientId.set("")
        self.PatientName.set("") 
        self.DateOfBirth.set("") 
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", "end")

    def exitWindow(self):
        exitWindow=messagebox.askyesno("EXIT", "Do you want to exit?")
        if exitWindow>0:
            window.destroy()
            return

    #Constructor

    def __init__(self, window):
        self.window = window
        self.window.title("Apollo Hospital")

        self.nameOftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.Numberoftablets = StringVar()
        self.doctor = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.StorageAdvice = StringVar()
        self.patientId = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.window, bd=20, relief = "ridge", text = "APOLLO HOSPITAL", fg = "#9FA8DA", bg = "white", font =("times new roman",50,"bold"), background="#555555")
        lbltitle.pack(side=TOP, fill=X)

        #Frame1
        
        frame1 = Frame(self.window, bd=20, relief = "ridge", bg="black")
        frame1.place(x=0,y=130,width=1530,height=400)

        frame2 = LabelFrame(frame1, bd=10,relief="ridge", padx=10, font=("calibri",12,"bold"), text ="Patient Details and Medication", bg="#E8EAF6")
        frame2.place(x=15, y=5, width =980, height=350)

        frame3 = LabelFrame(frame1, bd=10,relief="ridge", padx=10, font=("calibri",12,"bold"), text ="Prescription", bg="#E8EAF6")
        frame3.place(x=1015, y=5, width =460, height=350)

        #Frame2

        frame4 = Frame(self.window, bd=20, relief = "ridge", bg="black")
        frame4.place(x=0,y=530,width=1530,height=70)

        #frame5

        frame5 = Frame(self.window, bd=20, relief = "ridge", bg="black")
        frame5.place(x=0,y=600,width=1530,height=190)

        #Labels

        lblNameTablet=Label(frame2, text = "Names of Tablet", font=("times new roman", 12,"bold"),padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet=ttk.Combobox(frame2, textvariable=self.nameOftablets ,font=("times new roman", 12,"bold"),width =33)
        comNametablet["values"]=("Paracetamol", "Crocin", "Dolo", "MontairLC", "Meftal-Spas", "Cyclopam", "Okacet", "PAN-20")
        comNametablet.grid(row=0, column=1)

        lblref = Label(frame2, font=("arial",12,"bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(frame2, textvariable=self.ref, font=("arial", 13,"bold"), width=35)
        txtref.grid(row=1, column=1)

        lbldose = Label(frame2, font=("arial",12,"bold"), text="Dose:", padx=2, pady=4)
        lbldose.grid(row=2, column=0, sticky=W)
        txtdose = Entry(frame2, textvariable=self.Dose, font=("arial", 13,"bold"), width=35)
        txtdose.grid(row=2, column=1)

        lblNoOftablets = Label(frame2, font=("arial",12,"bold"), text="No of tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(frame2, textvariable=self.Numberoftablets, font=("arial", 13,"bold"), width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(frame2, font=("arial",12,"bold"), text="Doctor:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(frame2, textvariable=self.doctor, font=("arial", 13,"bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(frame2, font=("arial",12,"bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(frame2, textvariable=self.Issuedate, font=("arial", 13,"bold"), width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(frame2, font=("arial",12,"bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(frame2,textvariable=self.ExpDate, font=("arial", 13,"bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(frame2, font=("arial",12,"bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=6, column=2, sticky=W)
        txtDailyDose = Entry(frame2, textvariable=self.DailyDose, font=("arial", 13,"bold"), width=35)
        txtDailyDose.grid(row=6, column=3)

        lblStorage = Label(frame2, font=("arial",12,"bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=5, column=2, sticky=W)
        txtStorage = Entry(frame2, textvariable=self.StorageAdvice, font=("arial", 13,"bold"), width=35)
        txtStorage.grid(row=5, column=3)

        lblpatientId = Label(frame2, font=("arial",12,"bold"), text="Patient ID:", padx=2, pady=6)
        lblpatientId.grid(row=1, column=2, sticky=W)
        txtpatientId = Entry(frame2, textvariable=self.patientId, font=("arial", 13,"bold"), width=35)
        txtpatientId.grid(row=1, column=3)

        lblPatientname = Label(frame2, font=("arial",12,"bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientname.grid(row=2, column=2, sticky=W)
        txtPatientname = Entry(frame2, textvariable=self.PatientName, font=("arial", 13,"bold"), width=35)
        txtPatientname.grid(row=2, column=3)

        lblDateOfBirth = Label(frame2, font=("arial",12,"bold"), text="Date Of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=4, column=2, sticky=W)
        txtDateOfBirth = Entry(frame2, textvariable=self.DateOfBirth, font=("arial", 13,"bold"), width=35)
        txtDateOfBirth.grid(row=4, column=3)

        lblPatientAddress = Label(frame2, font=("arial",12,"bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=3, column=2, sticky=W)
        txtPatientAddress = Entry(frame2, textvariable=self.PatientAddress, font=("arial", 13,"bold"), width=35)
        txtPatientAddress.grid(row=3, column=3)

        #Prescription

        self.txtPrescription = Text(frame3, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #Buttons

        btnPrescription = Button(frame4, command=self.showPrescription, text="Show Prescription", bg="#1A237E", fg="white",font=("arial", 12, "bold"), width=23,  padx=2, pady=6)
        btnPrescription.grid(row=0, column=1)

        btnPrescriptionData = Button(frame4, command=self.addPrescription, text="Add Information", bg="#1A237E", fg="white",font=("arial", 12, "bold"), width=23,  padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=0)

        btnUpdate = Button(frame4, text="Update", command=self.updateData, bg="#1A237E", fg="white",font=("arial", 12, "bold"), width=23,  padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(frame4, text="Delete",command= self.delete, bg="#1A237E", fg="white",font=("arial", 12, "bold"), width=23,  padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(frame4, text="Clear", command= self.clearAll, bg="#1A237E", fg="white",font=("arial", 12, "bold"), width=23,  padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(frame4, command=self.exitWindow, text="Exit", bg="#1A237E", fg="white",font=("arial", 12, "bold"), width=23,  padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        #Database display

        scroll_x = ttk.Scrollbar(frame5, orient = "horizontal")
        scroll_y = ttk.Scrollbar(frame5, orient = "vertical")
        self.hospital_table = ttk.Treeview(frame5, column = ("nameoftable", "ref", "dose", "nooftablets", "doctor", "issuedate", "expdate", "dailydose", "storage", "patientId", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom", fill=X)
        scroll_y.pack(side="right", fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("doctor", text="Doctor")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("patientId", text="Patient ID")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill = "both", expand =1)

        self.hospital_table.column("nameoftable", width = 100)
        self.hospital_table.column("ref", width = 100)
        self.hospital_table.column("dose", width = 100)
        self.hospital_table.column("nooftablets", width = 100)
        self.hospital_table.column("doctor", width = 100)
        self.hospital_table.column("issuedate", width = 100)
        self.hospital_table.column("expdate", width = 100)
        self.hospital_table.column("dailydose", width = 100)
        self.hospital_table.column("storage", width = 100)
        self.hospital_table.column("patientId", width = 100)
        self.hospital_table.column("pname", width = 100)
        self.hospital_table.column("dob", width = 100)
        self.hospital_table.column("address", width = 100)

        self.hospital_table.pack(fill = "both", expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.myCursor)
        self.fetchData()

if __name__ == "__main__":
    window = Tk()
    myApp = Hospital(window)
    window.geometry('2900x850+0+0')
    window.mainloop()



