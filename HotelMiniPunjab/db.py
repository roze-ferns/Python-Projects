import sqlite3

con = sqlite3.connect('HOTEL.db')


cur = con.cursor()
 
cur.execute('CREATE TABLE HOTEL(customer_id INTEGER, table_id INTEGER, order_items STRING, total INTEGER, payment_opt STRING, Date STRING)')

#int(self.customer_id), int(self.tableid),str(self.order_items), int(self.total), str(self.payment_opt),str(self.fin_time)