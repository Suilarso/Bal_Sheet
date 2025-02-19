#Project: SJ transaksi sehari sehari - File ini untuk class yg lain2
#Date: Oct 22, 24


from ast import Pass
from tkinter import *
from urllib.request import proxy_bypass
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

#SJ3271124 - Class ini utk browsing data transaksi
class BrowsingTransactions:
    #def __init__(self, sjAcctDB):
    def  __init__(self, recData):
        self.recData = recData
        self.rowsPerPage = 10
        #self.numOfRow = 0
        self.numOfCol = 6
        self.totalRecords = len(self.recData)
        self.currentPage = 0
        self.pageFirstRecord = []
        self.currentRecord = 0
        self.totalRecordsBrowsed = 0
        self.curRowNumber = self.startRow = 2

        #print('recData ', self.totalRecords, recData)
        self.browseWindow = Toplevel()
        self.browseTable = SJTable(self.browseWindow, self.rowsPerPage, self.numOfCol)
        self.browsingScreenLayout()

    def browsingScreenLayout(self):
        #self.browseWindow
        #SJ3111224 - Use str(chr(923)) for up indicator and capital letter V for down indicator
        self.upButton = Button(self.browseWindow, text=str(chr(923)), command=lambda x=self.browseTable: self.upButtonCallback(x))
        self.upButton.grid(row=self.curRowNumber, column=0)
        self.cancelButton = Button(self.browseWindow, text='Cancel', command=lambda x=self.browseWindow, y=self.browseTable:
                                   self.cancelButtonCallback(x, y))
        self.cancelButton.grid(row=self.curRowNumber, column=self.numOfCol+1)
        self.curRowNumber += 1

        self.downButton = Button(self.browseWindow, text='V', command=lambda x=self.browseTable: self.downButtonCallback(x))
        self.downButton.grid(row=self.curRowNumber, column=0)
        self.selectButton = Button(self.browseWindow, text='Select', command=lambda x=self.browseWindow, y=self.browseTable:
                                   self.selectButtonCallback(x, y))
        self.selectButton.grid(row=self.curRowNumber, column=self.numOfCol+1)
        self.curRowNumber += 1
        
        self.prevPageButton = Button(self.browseWindow, text=str(chr(171)), command=lambda x=self.browseTable, y=self.recData: self.prevPageButtonCallback(x, y))
        self.prevPageButton.grid(row=self.curRowNumber, column=0)
        self.curRowNumber += 1
        self.nextPageButton = Button(self.browseWindow, text=str(chr(187)), command=lambda x=self.browseTable, y=self.recData: self.nextPageButtonCallback(x, y))
        self.nextPageButton.grid(row=self.curRowNumber, column=0)
        
        #SJ6040125 - re-intialize global var
        if (len(self.pageFirstRecord) != 0):
            del self.pageFirstRecord[:]
        self.totalRecordsBrowsed = 0

        self.numOfRow = self.rowsPerPage if self.totalRecords >= self.rowsPerPage else self.totalRecords
        self.currentRecord = 0  #SJ1090522 - valid value = 0 to numOfRow - 1
        self.currentPage = 0  #SJ5130522 - First page of records
        self.pageFirstRecord.append(0)  #SJ2100522 - 0 being the first record of the total searched records
        self.totalRecordsBrowsed += self.numOfRow
        print('numOfRow, pageFirstRecord, totalRecordsBrowsed: ', self.numOfRow, self.pageFirstRecord, self.totalRecordsBrowsed)
        
        for i in range(self.numOfRow):
            self.browseTable.addRowOfData(i, self.recData[i])

        self.browseTable.highlightRow(self.currentRecord, self.numOfCol)

    def upButtonCallback(self):
        #SJ3080125 - Can only move up if currentRecord is not pointing to first record of the table
        if self.currentRecord > 0:
            self.browseTable.deHighlightRow(self.currentRecord, self.numOfCol)
            self.currentRecord -= 1
            self.browseTable.highlightRow(self.currentRecord, self.numOfCol)
        else:
            pass

    def downButtonCallback(self):
        #SJ3080125 - Can only move down if currentRecord is not pointing to the last record of the table
        if self.currentRecord < (self.numOfRow - 1):
            self.browseTable.deHighlightRow(self.currentRecord, self.numOfCol)
            self.currentRecord += 1
            self.browseTable.highlightRow(self.currentRecord, self.numOfCol)
        else:
            pass

    def prevPageButtonCallback(self):
        #SJ3080125 - Can go back to previous page if only current page is beyond first page
        if self.currentPage != 0:
            del self.pageFirstRecord[self.currentPage]  #SJ3080125 - remove the first record of current page before going back to previous page
            self.currentPage -= 1
            self.totalRecordsBrowsed -= self.numOfRow
            self.currentRecord = 0

            #SJ3080125 - Clear table before populating the table with new page of data
            self.browseTable.clearTable(self.numOfRow, self.numOfCol)
            self.numOfRow = self.rowsPerPage
            for i in range(self.numOfRow):
                self.browseTable.addRowOfData(i, self.recData[self.pageFirstRecord[self.currentPage] + i])
            self.browseTable.highlightRow(self.currentRecord, self.numOfCol)

        print('currentPage, numOfRow, pageFirstRecord, totalRecordsBrowsed: ',
               self.currentPage, self.numOfRow, self.pageFirstRecord, self.totalRecordsBrowsed)

    def nextPageButtonCallback(self):
        #SJ3080125 - Computer how many records left available for display
        availRecord = self.totalRecords - self.totalRecordsBrowsed
        if availRecord == 0:
            #SJ3080125 - If comes here, means no more records available for browsing
            pass
            #return
        else:
            #SJ3080125 - If comes here, means there are still records to be displayed
            self.currentRecord = 0
            self.numOfRow = self.rowsPerPage if availRecord >= self.rowsPerPage else availRecord
            self.pageFirstRecord.append(self.pageFirstRecord[self.currentPage] + self.rowsPerPage)
            self.currentPage += 1
            self.totalRecordsBrowsed += self.numOfRow

            #SJ3080125 - Clear table before populating the table with new page of data
            self.browseTable.clearTable(self.rowsPerPage, self.numOfCol)
            for i in range(self.numOfRow):
                self.browseTable.addRowOfData(i, self.recData[self.pageFirstRecord[self.currentPage] + i])
            self.browseTable.highlightRow(self.currentRecord, self.numOfCol)

            print('currentPage, numOfRow, pageFirstRecord, totalRecordsBrowsed: ',
                   self.currentPage, self.numOfRow, self.pageFirstRecord, self.totalRecordsBrowsed)

    def cancelButtonCallback(self, browseWindow, browseTable):
        #self.browseButton.configure(state=NORMAL)
        del(self.browseTable)
        self.browseWindow.destroy()

    def selectButtonCallback(self, browseWindow, browseTable):
        pass

    def __del__(self):
        print('Destructor untuk BrowsingTransactions object')



