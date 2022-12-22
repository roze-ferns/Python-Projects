from tkinter import *
import sqlite3
from time import strftime
import random as r

con = sqlite3.connect('HOTEL.db')
cur = con.cursor()

class Hotel:
	def __init__(self,parent):
	#1
		cur.execute('SELECT * FROM HOTEL')
		self.parent=parent
		self.parent.title('HOTEL MINI PUNJAB')
		self.hotel_menu={'Aloo Paratha':100,'Veg Platter':150,'Dal Makhni':170,'Paneer Kofta':220,'Butter Naan':40,'Hyderabadi Biryani':280}
		self.display_menu=[]
		for i in self.hotel_menu:
			self.display_menu.append(str(f"{i}-{self.hotel_menu[i]}"))
		self.frame_1=Frame(parent)
		self.frame_1.grid()
		self.frame_2=Frame(self.frame_1,height=250,width=250,borderwidth=3, bg="light grey")
		self.frame_2.grid()
		self.total=0
		self.table_total=[]
		for i in range(1,6):
			self.table_total.append(i)
		self.order_placed=False		
		self.order_items=[]  
		self.parent.resizable(False, False)
		self.frame_3=Frame(parent,height=250,width=250,borderwidth=3, bg="light blue")
		self.frame_3.grid(row=1,column=0)
		self.frame_3=Frame(parent,height=500,width=350,borderwidth=3, bg="light blue")
		self.frame_3.grid(row=0,column=1,rowspan=2)
		self.frame_4=Frame(parent,height=250,width=250,borderwidth=3, bg="blue")
		self.frame_4.grid(row=1,column=0)
		# self.tableid=r.randint(1,5)
		
  

    #2
		self.choose_item=StringVar(self.frame_2)
		self.choose_item.set('Select Item')		
		self.label=Label(self.frame_2,text='MENU',font=('Arial',15),bd=6, bg="blue")
		self.label.place(relx=0.1,rely=0.11,width=200)
		self.options=OptionMenu(self.frame_2,self.choose_item,*self.display_menu)
		self.options.config(font=('Arial',14))
		self.options.place(relx=0.5,rely=0.4,anchor='center')
		menu = self.frame_2.nametowidget(self.options.menuname)
		menu.config(font=('Arial',13))
		self.add_button=Button(self.frame_2,text="Add",font=('Arial',14),height='1', width='15',command=lambda:self.add_function())
		self.add_button.place(relx=0.15,rely=0.6)
  
    #3
		int1=IntVar()
		int1.set(4)
		self.label_customer_Id=Label(self.frame_3,text='Customer ID',font=('Arial',12))
		self.label_customer_Id.place(relx=0.1,rely=0.04)
		self.entry_customer_Id=Entry(self.frame_3,borderwidth=2,width=17,font=('Arial',12))
		self.entry_customer_Id.place(relx=0.5,rely=0.02,height=40)
		self.label_table_no=Label(self.frame_3,text='Table (1-5)',font=('Arial',12))
		self.label_table_no.place(relx=0.1,rely=0.14)
		#self.labelallot=Entry(self.frame_3,text=self.tableid,borderwidth=2,width=16,font=('Arial',13), background="white")
		self.labelallot=Entry(self.frame_3,borderwidth=2,width=16,font=('Arial',13))
		self.labelallot.place(relx=0.5,rely=0.12,height=40,width=160)
		self.label=Label(self.frame_3,text='Date',font=('Arial',12), width=6)
		self.label.place(relx=0.1,rely=0.24)

		self.labelt=Label(self.frame_3,borderwidth=2,width=17,font=('Arial',13), background="white")
		self.labelt.place(relx=0.5,rely=0.22,height=40)
		self.update_time()
		self.label=Label(self.frame_3,text='Bill',font=('Arial',12), width=6)
		self.label.place(relx=0.1,rely=0.40)
		self.labelf=Listbox(self.frame_3,borderwidth=2,font=('Arial',13),selectmode=MULTIPLE)
		self.labelf.place(relx=0.3,rely=0.32,width=230,height=156)
		self.label=Label(self.frame_3,text='Total',font=('Arial',13), width=9, height=1)
		self.label.place(relx=0.54,rely=0.64)
		self.labeltotal=Label(self.frame_3,text="0",borderwidth=2,height=1,width=6,font=('Arial',13))
		self.labeltotal.place(relx=0.79,rely=0.64)
		self.button=Button(self.frame_3,text='Delete',font=('Arial',11),command=lambda:self.delete_selected(), width=1, height=1)
		self.button.place(relx=0.30,rely=0.637,width=100)
		self.button=Button(self.frame_3,text='Close',font=('Arial',12),command=lambda:self.closew())
		self.button.place(relx=0.5,rely=0.9,width=120)
		self.payment=StringVar()
		self.payment.set("Pay By")
		self.options1=OptionMenu(self.frame_3,self.payment,'Cash','Card', 'UPI')
		self.options1.config(font=('Arial',12))
		self.options1.place(relx=0.5,rely=0.76,anchor='center')
		menu = self.frame_3.nametowidget(self.options1.menuname)
		menu.config(font=('Arial',13))
		self.buttonconf=Button(self.frame_3,text='Confirm',font=('Arial',12),command=lambda:self.order_whole())
		self.buttonconf.place(relx=0.35,rely=0.80,width=100)
		self.buttonnew_order=Button(self.frame_3,text='Next',font=('Arial',12),command=lambda:self.new_order())
		self.buttonnew_order.place(relx=0.15,rely=0.9,width=100)
		self.choice_list=StringVar(self.frame_3)
		self.choice_list.set(self.labelf.curselection())
        
    #4
		self.table_search=StringVar()
		self.table_search.set('Select Table')
        
		self.label=Label(self.frame_4,text='Table',font=('Arial',13), width=8)
		self.label.place(relx=0.0,rely=0.15)
		self.options2=OptionMenu(self.frame_4,self.table_search,*self.table_total)
		self.options2.config(font=('Arial',11))
		self.options2.place(relx=0.35,rely=0.12,height=40,width=160)
		self.date=Label(self.frame_4,text='Date',font=('Arial',13), width=8)
		self.date.place(relx=0.0,rely=0.43)
		self.datesel1=Entry(self.frame_4,borderwidth=2,font=('Arial',13))
		self.datesel1.place(relx=0.35,rely=0.4,height=40,width=50)
		self.datesel2=Entry(self.frame_4,borderwidth=2,font=('Arial',13))
		self.datesel2.place(relx=0.575,rely=0.4,height=40,width=50)
		self.datesel3=Entry(self.frame_4,borderwidth=2,font=('Arial',13))
		self.datesel3.place(relx=0.795,rely=0.4,height=40,width=50)
		
		self.button=Button(self.frame_4,text='Data till now', width=23 ,font=('Arial',11),command=lambda:self.show_results())
		self.button.place(relx=0.05,rely=0.7)

	def update_time(self):
		self.date=strftime('%d/%m/%y')
		self.time=strftime('%H:%M')
		if self.order_placed!=True:
			self.labelt.config(text=self.date+" "+self.time)
			self.fin_time=str(strftime('%y%m%d')+self.time)
			self.labelt.after(1000*60,self.update_time)
	
	def delete_selected(self):
		selected_item= self.labelf.curselection()
		for item in selected_item[::-1]:
			self.labelf.delete(item)
		self.display_total()
		
	def add_function(self):
		try:
			if(int(self.choose_item.get()[self.choose_item.get().index('-')+1:])>0):
				self.labelf.insert(END,str(self.choose_item.get()))
				self.display_total()
		except:
			k=1
	def closew(self):
		self.parent.destroy()
	def display_total(self):
		self.items=self.labelf.get(0,END)
		self.total=0
		for i in self.items:
			a=int(i[i.index('-')+1:])
			self.total+=a
		if self.total>0 and self.order_placed==False:
			self.buttonconf.config(state=NORMAL)
		self.labeltotal.config(text=''+str(self.total))
	def order_whole(self):
		self.customer_id=self.entry_customer_Id.get()		
		self.table_id=self.labelallot.get()		
		self.final_date=str(self.date)
		for i in self.items:
			a=i[:i.index('-')]
			self.order_items.append(a)
		self.payment_opt=self.payment.get()[3:]
		cur.execute('''INSERT INTO HOTEL VALUES (?,?,?,?,?,?);''',(int(self.customer_id), int(self.table_id),str(self.order_items), int(self.total), str(self.payment_opt),str(self.fin_time)))
		con.commit()
		self.choose_item.set('Choose an option')
		self.order_placed=True
		self.payment.set("Pay By")
		self.timestop=str(self.labelt['text'])
		self.labelt.config(text=self.timestop)

		
	def show_results(self):
		try:
			if 0<int(self.datesel1.get())<=31 and 0<int(self.datesel2.get())<=12 and 0<int(self.datesel1.get())<=99:
				self.date_search=self.datesel3.get()+self.datesel2.get()+self.datesel1.get()
		except:
			k=1
			return
		if self.table_search.get()!='Select Table':
			cur.execute("SELECT * FROM HOTEL WHERE (table_id = ? AND Date >= ?) ",(int(self.table_search.get()),str(self.date_search),))
			q=cur.fetchall()
			new= Toplevel(self.parent)
			new.geometry("750x250")
			new.title("Results")
			text1=str()
			label=Label(new,text=text1)
			label.pack(anchor='nw')
			total_earn=0
			for i in q:
				total_earn+=i[3]
				date1=i[-1]
				date1=f"{date1[6:]} {date1[4:6]}/{date1[2:4]}/{date1[:2]}"
				text1+=f"Customer ID : {i[0]}; Table : {i[1]}; Order : {i[2]}; Total : {i[3]}; Date : {date1}\n"
				label.config(text=text1)
			label2=Label(new,text="Total Earned : " + str(total_earn),font=('Arial',18))
			label2.pack(side=BOTTOM)
			
		else:
			return
		new.title(f'All Orders since {self.datesel1.get()}/{self.datesel2.get()}/{self.datesel3.get()}')
		self.datesel1.delete(0,END)
		self.datesel2.delete(0,END)
		self.datesel3.delete(0,END)
		self.table_search.set('Select Table')
	def new_order(self):
		self.total=0
		# a=r.randint(1,5)
		# while(a==self.tableid):
		# 	a=r.randint(1,5)
		self.labelallot.delete(0,END) #try
		self.labelf.delete(0,END)
		self.entry_customer_Id.delete(0,END)
		self.labeltotal.config(text='0')
		self.labelallot.config(text="")
		
		
if __name__=='__main__':
	window=Tk()
	myapp=Hotel(window)
	window.mainloop()
