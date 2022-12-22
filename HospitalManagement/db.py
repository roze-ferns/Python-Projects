import sqlite3

con = sqlite3.connect('HOSPITAL.db')

cur = con.cursor()
 
cur.execute('CREATE TABLE HOSPITAL(nameOfTablets STRING,referenceNo STRING PRIMARY KEY,  dose STRING, numberOfTablets STRING, doctor STRING, issueDate STRING, expDate STRING, dailyDose STRING, storage STRING, patientId STRING, patientName STRING, DOB STRING, patientAddress STRING)')




#cur.execute('CREATE TABLE HOSPITAL(ID INT PRIMARY KEY, nameOfTablets STRING, referenceNo STRING, dose STRING, numberOfTablets STRING, doctor STRING, issueDate STRING, expDate STRING, dailyDose STRING, storage STRING, nhsNumber STRING, patientName STRING, DOB STRING, patientAddress STRING)')

#int(self.ID), str(self.nameOfTablets),str(self.referenceNo), str(self.dose), str(self.numberOfTablets),str(self.doctor), str(self.issueDate),str(self.expDate), str(self.dailyDose), str(self.storage),str(self.nhsNumber), str(self.patientName),str(self.DOB), str(self.patientAddress)                                                      