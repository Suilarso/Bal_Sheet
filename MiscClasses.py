#Project: SJ transaksi sehari sehari - File ini untuk class yg lain2
#Date: Oct 22, 24


from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

#SJ2221024 - This class prompts user for a date and return the date to the calling function
class SelectDateDialog:
    def __init__(self, master, dialogText):
        self.dateDialog = Toplevel(master)
        #self.fromDate = '0'
        self.fromDate = str(datetime(1,1,1).now())[:10]  #SJ2221024 - Only need the date portion
        #SJ2221024 - Input field for Date received
        self.todayDate = datetime(1,1,1).now()  #SJ1250422 - Getting today system date
        #self.dateReceivedLabel = Label(self.dateDialog, text='Please select the date you wish to browse the record from').grid(row=2, column=1)
        self.dateReceivedLabel = Label(self.dateDialog, text=dialogText).grid(row=2, column=1)
        self.dateReceived = DateEntry(self.dateDialog, values="Text", year=self.todayDate.year, state="readonly", date_pattern="yyyy-mm-dd")
        self.dateReceived.grid(row=4, column=1, padx=20, pady=5, sticky=W)

        self.okButton = Button(self.dateDialog, text="Ok", command = self.okCallback)
        self.okButton.grid(row=4, column=2)

    def okCallback(self):
        self.fromDate = self.dateReceived.get_date()
        self.dateDialog.destroy()

    def getFromDate(self):
        return (self.fromDate)
        #return (self.fromDate[:10])

    def __del__(self):
        print('Destructor for selectDateDialog')

#SJ2221024 - Class to create table
class SJTable:
    def __init__(self, master, numOfRow, numOfCol):
        self.browseTable = master #Toplevel(master)
        self.entryFields = [[0 for x in range(numOfCol)] for y in range(numOfRow)]
        self.rowNumber = 2
        #self.label = Label(master, text='Records Browser')
        #self.label.grid(row=0, column=0)
        # code for creating table
        for i in range(numOfRow):
            for j in range(numOfCol):
                #self.e = Entry(self.browseTable, width=20, fg='blue', font=('Arial',16,'bold'))
                self.e = Entry(self.browseTable, width=20, fg='black', font=('Arial',12))
                self.e.grid(row=self.rowNumber+i, column=1+j)
                self.entryFields[i][j] = self.e

    def addRowOfData(self, rowNumber, recData):
        #SJ2221024 - seq of input data: workOrder, customerName, dateReceived
        self.entryFields[rowNumber][0].insert(0, recData[0])
        self.entryFields[rowNumber][0].configure(state=DISABLED)
        self.entryFields[rowNumber][1].insert(0, recData[1])
        self.entryFields[rowNumber][1].configure(state=DISABLED)
        #self.entryFields[rowNumber][2].set_date(recData[2])
        self.entryFields[rowNumber][2].insert(0, recData[2])
        self.entryFields[rowNumber][2].configure(state=DISABLED)

    def highlightRow(self, rowNumber, numOfCol):
        for i in range(numOfCol):
            self.entryFields[rowNumber][i].configure(state=NORMAL, bg='green')  #'#A202FF'

    def deHighlightRow(self, rowNumber, numOfCol):
        for i in range(numOfCol):
            self.entryFields[rowNumber][i].configure(state=DISABLED)

    def clearTable(self, numOfRow, numOfCol):
        for i in range(numOfRow):
            for j in range(numOfCol):
                self.entryFields[i][j].configure(state=NORMAL, bg='white')
                self.entryFields[i][j].delete(0, END)

    def getWorkOrder(self, currentRecord):
        return (self.entryFields[currentRecord][0].get())

    def __del__(self):
        #SJ2221024 - Need to add code to call destroy() method
        print('Destructor for SJTable')




