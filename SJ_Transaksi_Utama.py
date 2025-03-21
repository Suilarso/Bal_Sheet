#Project: SJ transaksi sehari sehari
#Date: Mar 30, 23

from tkinter import *
from tkinter.messagebox import *
from tkcalendar import DateEntry  #SJ4300524 - 
from datetime import datetime  #SJ2280524
from MainAccount import MainAccount
from SubAccount import SubAccount
from BankAccount import BankAccount
from MiscClasses import SelectDateDialog
from MiscClasses import SJTable  #SJ1111124 - SJTable class
from MiscClasses import BrowsingTransactions 
import sqlite3


#SJ1270523 - This class setup GUI for daily transaction entry screen.
#SJ1270524 - The data keyed in the entry screen are to be saved in sjAcct table
class SjAccount():
    def __init__(self, mainWidget, mainAcctDB, subAcctDB, bankAcctDB, sjAcctDB):
        self.sjAcctWidget = mainWidget
        self.sjAcctWidget.geometry("750x500")
        self.sjAcctDB = sjAcctDB
        self.transDate = datetime(1,1,1).now()  #SJ1270524 - Getting today system date
        self.date = ''
        self.mainAcctOptionList = ''
        self.mainAcctOption = ''
        self.mainAcctDropdown = ''
        self.subAcctOptionList = ''
        self.subAcctOption = ''
        self.subAcctDropdown = ''
        self.beaconOptionList = ''
        self.beaconOption = ''
        self.beaconOptionDropdown = ''
        self.amount = 0.0
        self.db_crOptionList = ''
        self.db_crOption = ''
        self.db_crOptionDropdown = ''
        self.postToOptionList = ''
        self.postToOption = ''
        self.postToOptionDropdown = ''
        self.status = ''
        self.remark = ''

        #SJ2280524 - Local variables for X-Y coordinate
        self.leftMargin = 5
        self.topMargin = 5
        self.rowGapConstant = 10
        self.fieldHeightConstant = 22
        self.labelEntryGap = 125
        
        self.transDateLabelX = self.leftMargin
        self.transDateLabelY = self.topMargin
        self.transDateEntryX = self.transDateLabelX + self.labelEntryGap
        self.transDateEntryY = self.transDateLabelY  #Col 2
        self.transDateEntryWidth = 98

        self.mainAcctLabelX = self.leftMargin
        self.mainAcctLabelY = self.transDateLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.mainAcctEntryX = self.mainAcctLabelX + self.labelEntryGap
        self.mainAcctEntryY = self.mainAcctLabelY
        self.mainAcctEntryWidth = 100
        
        self.subAcctLabelX = self.leftMargin
        self.subAcctLabelY = self.mainAcctLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.subAcctEntryX = self.subAcctLabelX + self.labelEntryGap
        self.subAcctEntryY = self.subAcctLabelY
        self.subAcctEntryWidth = 100
       
        self.beaconLabelX = self.leftMargin
        self.beaconLabelY = self.subAcctLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.beaconEntryX = self.beaconLabelX + self.labelEntryGap
        self.beaconEntryY = self.beaconLabelY
        self.beaconEntryWidth = 80

        self.amountLabelX = self.leftMargin
        self.amountLabelY = self.beaconLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.amountEntryX = self.amountLabelX + self.labelEntryGap
        self.amountEntryY = self.amountLabelY
        self.amountEntryWidth = 50

        self.db_crLabelX = self.leftMargin
        self.db_crLabelY = self.amountLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.db_crEntryX = self.db_crLabelX + self.labelEntryGap
        self.db_crEntryY = self.db_crLabelY
        self.db_crEntryWidth = 80

        self.postToLabelX = self.leftMargin
        self.postToLabelY = self.db_crLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.postToEntryX = self.postToLabelX + self.labelEntryGap
        self.postToEntryY = self.postToLabelY
        self.postToEntryWidth = 100

        self.statusLabelX = self.leftMargin
        self.statusLabelY = self.postToLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.statusEntryX = self.statusLabelX + self.labelEntryGap
        self.statusEntryY = self.statusLabelY
        self.statusEntryWidth = 50

        self.remarkLabelX = self.leftMargin
        self.remarkLabelY = self.statusLabelY + self.fieldHeightConstant + self.rowGapConstant
        self.remarkEntryX = self.remarkLabelX + self.labelEntryGap
        self.remarkEntryY = self.remarkLabelY
        self.remarkEntryWidth = 250

        self.cancelButtonX = self.leftMargin + 60
        self.cancelButtonY = self.remarkLabelY + self.fieldHeightConstant + self.rowGapConstant + self.rowGapConstant
        self.cancelButtonWidth = 60
        self.saveButtonX = self.cancelButtonX + 150
        self.saveButtonY = self.remarkLabelY + self.fieldHeightConstant + self.rowGapConstant + self.rowGapConstant
        self.saveButtonWidth = 50

        self.setupDropdownList()
        self.setupSjAcctScreen()

    def setupDropdownList(self):
        """This method create all dropdown lists (Main Acct, Sub Acct, Beacon, and Post to) needed in the GUI"""
        self.mainAcctOptionList = mainAcctDB.readAllRecords("mainAcct")
        self.subAcctOptionList = subAcctDB.readAllRecords("subAcct")
        self.beaconOptionList = ["Needs", "Wants", "Saving"]
        self.db_crOptionList = ["Debit", "Credit"]
        self.postToOptionList = bankAcctDB.readAllRecords("bankCode")

    def setupSjAcctScreen(self):
        """This method is used to setup data entry screen for SJ Account. It contains nine fields: Date, Main Acct, Sub-acct, beacon, 
           Amount, db_cr, Post to, Status, and Remark."""
    
        #SJ4300524 - Input field for transaction Date
        self.transDate = datetime(1,1,1).now()  #SJ4300524 - Getting today system date
        self.transDateLabel = Label(self.sjAcctWidget, text='Transaction Date: ').place(x=self.transDateLabelX, y=self.transDateLabelY)
        self.date = DateEntry(self.sjAcctWidget, values="Text", year=self.transDate.year, state="readonly", date_pattern="yyyy-mm-dd")
        self.date.place(x=self.transDateEntryX, y=self.transDateEntryY, width = self.transDateEntryWidth, height = self.fieldHeightConstant)

        #SJ2280524 - Main Account field
        self.mainAcctLabel = Label(self.sjAcctWidget, text='Main Acct: ').place(x=self.mainAcctLabelX, y=self.mainAcctLabelY)
        self.mainAcctOption = StringVar(self.sjAcctWidget)
        self.mainAcctOption.set(self.mainAcctOptionList[0])
        self.mainAcctDropdown = OptionMenu(self.sjAcctWidget, self.mainAcctOption, *self.mainAcctOptionList)
        self.mainAcctDropdown.place(x=self.mainAcctEntryX, y=self.mainAcctEntryY, width=self.mainAcctEntryWidth, height=self.fieldHeightConstant+3)
        
        #SJ4060624 - Sub Account field
        self.subAcctLabel = Label(self.sjAcctWidget, text='Sub Acct: ').place(x=self.subAcctLabelX, y=self.subAcctLabelY)
        self.subAcctOption = StringVar(self.sjAcctWidget)
        self.subAcctOption.set(self.subAcctOptionList[0])
        self.subAcctDropdown = OptionMenu(self.sjAcctWidget, self.subAcctOption, *self.subAcctOptionList)
        self.subAcctDropdown.place(x=self.subAcctEntryX, y=self.subAcctEntryY, width=self.subAcctEntryWidth, height=self.fieldHeightConstant+3)
        
        #SJ4060624 - Beacon field
        self.beaconLabel = Label(self.sjAcctWidget, text='Beacon: ').place(x=self.beaconLabelX, y=self.beaconLabelY)
        self.beaconOption = StringVar(self.sjAcctWidget)
        self.beaconOption.set(self.beaconOptionList[0])
        self.beaconOptionDropdown = OptionMenu(self.sjAcctWidget, self.beaconOption, *self.beaconOptionList)
        self.beaconOptionDropdown.place(x=self.beaconEntryX, y=self.beaconEntryY, width=self.beaconEntryWidth, height=self.fieldHeightConstant+3)
        
        #SJ1100624 - Amount field
        #SJ2160724 - This input field needs to be validated for input that is convertible to int or float 
        self.amountLabel = Label(self.sjAcctWidget, text='Amount: ').place(x=self.amountLabelX, y=self.amountLabelY)
        self.amount = Entry(self.sjAcctWidget)
        self.amount.place(x=self.amountEntryX, y=self.amountEntryY, width=self.amountEntryWidth, height=self.fieldHeightConstant)
        
        #SJ1100624 - Debit / Credit field
        self.db_crLabel = Label(self.sjAcctWidget, text='Debit / Credit: ').place(x=self.db_crLabelX, y=self.db_crLabelY)
        self.db_crOption = StringVar(self.sjAcctWidget)
        self.db_crOption.set(self.db_crOptionList[0])
        self.db_crOptionDropdown = OptionMenu(self.sjAcctWidget, self.db_crOption, *self.db_crOptionList)
        self.db_crOptionDropdown.place(x=self.db_crEntryX, y=self.db_crEntryY, width=self.db_crEntryWidth, height=self.fieldHeightConstant+3)
        
        #SJ2110624 - Post To field
        self.postToLabel = Label(self.sjAcctWidget, text='Post To: ').place(x=self.postToLabelX, y=self.postToLabelY)
        self.postToOption = StringVar(self.sjAcctWidget)
        self.postToOption.set(self.postToOptionList[0])
        self.postToOptionDropdown = OptionMenu(self.sjAcctWidget, self.postToOption, *self.postToOptionList)
        self.postToOptionDropdown.place(x=self.postToEntryX, y=self.postToEntryY, width=self.postToEntryWidth, height=self.fieldHeightConstant+3)
        
        #SJ2110624 - Status field
        self.statusLabel = Label(self.sjAcctWidget, text='Status: ').place(x=self.statusLabelX, y=self.statusLabelY)
        self.status = Entry(self.sjAcctWidget)
        self.status.place(x=self.statusEntryX, y=self.statusEntryY, width=self.statusEntryWidth, height=self.fieldHeightConstant)
        
        #SJ2110624 - Remark field
        self.remarkLabel = Label(self.sjAcctWidget, text='Remark: ').place(x=self.remarkLabelX, y=self.remarkLabelY)
        self.remark = Entry(self.sjAcctWidget)
        self.remark.place(x=self.remarkEntryX, y=self.remarkEntryY, width=self.remarkEntryWidth, height=self.fieldHeightConstant)

        #SJ3240724 - Cancel and Save button
        #self.cancelButton = Button(text='Cancel', command=lambda x=self.sjAcctWidget: self.cancelButtonCallback(x))
        self.cancelButton = Button(self.sjAcctWidget, text="Cancel", command = self.cancelButtonCallback)
        self.cancelButton.place(x=self.cancelButtonX, y=self.cancelButtonY, width=self.cancelButtonWidth, height=self.fieldHeightConstant)
        #self.saveButton = Button(text='Save', command=lambda x=self.sjAcctWidget: self.saveButtonCallback(x))
        self.saveButton = Button(self.sjAcctWidget, text="Save", command = self.saveButtonCallback)
        self.saveButton.place(x=self.saveButtonX, y=self.saveButtonY, width=self.saveButtonWidth, height=self.fieldHeightConstant)

    def initializeSjAcctScreen(self):
        self.transDate = datetime(1,1,1).now()  #SJ4300524 - Getting today system date
        self.date.set_date(str(self.transDate.strftime("%Y-%m-%d")))
        self.mainAcctOption.set(self.mainAcctOptionList[0])
        self.subAcctOption.set(self.subAcctOptionList[0])
        self.beaconOption.set(self.beaconOptionList[0])
        self.amount.delete(0, END)
        self.db_crOption.set(self.db_crOptionList[0])
        self.postToOption.set(self.postToOptionList[0])
        self.status.delete(0, END)
        self.remark.delete(0, END)

    def verifySjAcctData(self):
        #SJ2060824 - Kita check apa data yg di isi di kotak amount valid sebagai float value
        tempAmount = self.amount.get().strip()
        retValue = True
        try:
            #SJ2060824 - Uji coba ganti data ke integer
            amount = int(tempAmount)
        except ValueError:
            try:
                #SJ2060824 Uji coba ganti data ke float
                amount = float(tempAmount)
            except ValueError:
                showerror(title="Invalid data", message="Data must be integer or float.")
                retValue = False

        return retValue

    def cancelButtonCallback(self):
        self.initializeSjAcctScreen()
        pass

    def saveButtonCallback(self):
        #SJ1290724 - Sebelum data yg tercantum di gui layar di saved ke sjAcctDb, data dari amount field perlu di check validity nya
        
        if (self.verifySjAcctData()):
            tempKey = self.mainAcctOption.get()+str(self.transDate)[:10]+str(self.transDate)[11:19]
            #print("tempAmt: ", isinstance(tempAmt, (int, float)))
            #print("transDate: {0}, mainAcctOption: {1}, subAcctOption: {2}, beaconOption: {3}".format(self.date.get_date(), self.mainAcctOption.get(), self.subAcctOption.get(), self.beaconOption.get()))
            #print("amount: {0}, db_crOption: {1}, postToOption: {2}, status: {3}, remark: {4}".format(eval(self.amount.get()), self.db_crOption.get(), self.postToOption.get(), self.status.get(), self.remark.get()))
            self.sjAcctDB.saveRecords(tempKey, self.date.get_date(), self.mainAcctOption.get(), self.subAcctOption.get(), self.beaconOption.get(), 
                                      eval(self.amount.get()), self.db_crOption.get(), self.postToOption.get(), self.status.get(), self.remark.get())
            self.initializeSjAcctScreen()
 
    def __del__(self):
        print('Destructor for SjAccount class')

#SJ1170423 - This class attempt to setup an sql connection
class SetupSQLConnection():
    def __init__(self, sqlFile, tableName, structList):
        self.conn = ''
        self.tableCursor = ''
        self.dbaseName = sqlFile
        self.tableName = tableName
        self.structList = structList
        self.establishConnection(sqlFile)

    def establishConnection(self, dbaseName):
        try:
            #print('Inside SetupSQLConnection: ', dbaseName)
            self.conn = sqlite3.connect(dbaseName)
            self.tableCursor = self.conn.cursor()
            #self.getSQLCursor()
        except:
            print('Fail to connect to database')
            #SJ3190423 - To implement a method to clean up un-successfull sql connection
            #quitter_function()
        #SJ6170623 - Try to add finally clause and see the result

    def getSQLCursor(self):
        return self.tableCursor

    def readAllRecords(self, field):
        sql = "SELECT "+field+" FROM "+self.tableName
        self.tableCursor.execute(sql)
        retList = [row[0] for row in self.tableCursor]
        return retList
        #print('retList: {0}'.format(retList))

    def readRecord(self, field, token):
    #SJ3130422 - Here we check for duplicate workOrder

        #sql = "SELECT "+field+" FROM "+self.tableName+" WHERE "+field+" = ? LIMIT 1"
        sql = "SELECT "+field+" FROM "+self.tableName+" WHERE "+field+" = ?"
        self.tableCursor.execute(sql, (token, ))
        #readData = self.tableCursor.fetchone()  #SJ0121123 - if use fetchone can use None to check
        readData = self.tableCursor.fetchall()  #SJ0121123 - if use fetchall check using len
        #totalRecords = len(readData)
        print('Inside readRecord: ', readData)        
        return readData

    #SJ3301024 - This method does a complex record retrieval
    def complexRead(self, fields, conditonClause, tokens):
        sql = "SELECT "+fields+" FROM "+self.tableName+" WHERE "+conditonClause
        self.tableCursor.execute(sql, tokens)
        recData = self.tableCursor.fetchall()  #SJ0010522 - if use fetchall check using len
        print("recData: ", recData)
        return recData

    def saveRecords(self, *data):
        #SJ2060623 - Construct string consisting of record structure of the table to save to
        fieldsStruct = ' ('
        valList = ' VALUES ('
        for item in self.structList:
            fieldsStruct = fieldsStruct[:] + item + ', '
            valList = valList[:] + '?' + ', '
        fieldsStruct = fieldsStruct[:-2]+')'
        valList = valList[:-2]+')'

        sql = "INSERT INTO "+self.tableName+fieldsStruct+valList
        self.tableCursor.execute(sql, data)
        self.conn.commit()

    def closeConnection(self):
        self.conn.close()

    def __del__(self):
        print('Destructor for SetupSQLConnection class: ', self.tableName)

def quitter_function():
    print('quitter_function: Closing sql connection and destroy root object...')
    #conn.close()  #SJ5310323 - Close database connection, to be un-remarked
    mainWindow.destroy()

#SJ3180924 - This function creates main menu
def mainMenu(root):
    menu = Menu()
    root.config(menu=menu)
    accounts_menu = Menu(menu, tearoff=0)
    accounts_menu.add_command(label='Main Account', command=lambda accountType="Main": accountsCallback(accountType))
    accounts_menu.add_command(label='Sub Account', command=lambda accountType="Sub": accountsCallback(accountType))
    accounts_menu.add_command(label='Bank Account', command=lambda accountType="Bank": accountsCallback(accountType))
    accounts_menu.add_command(label='Monthly Transaction', command = monthlyTransactionCallback)
    #accounts_menu.add_command(label='Main Account', command=accountsCallback)
    #accounts_menu.add_command(label='Sub Account', command=accountsCallback)
    #accounts_menu.add_command(label='Bank Account', command=accountsCallback)
    accounts_menu.add_separator()
    #SJ4031024 - SJTODO: find out the effect of quitter_function being called from menu window; concern is in the
    #SJ4031024 - quitter_function when called main window will be destroyed while mainWindow is still being used
    accounts_menu.add_command(label='Exit', command=quitter_function)
    menu.add_cascade(label='Account', menu=accounts_menu)

#SJ0201024 - General callback function for Main account, Sub account, and Bank account
def accountsCallback(accountType):
    print("Inside accountsCallback")
    mainAcctWindow = Toplevel()
    #mainAcctWindow.geometry("200x150")
    mainAcctWindow.lift()
    mainAcctWindow.grab_set()
    if accountType == "Main":
        mainAcctWindow.title('Main Account')
        mainAcctApp = MainAccount(mainAcctWindow, mainAcctDB)
    elif accountType == "Sub":
        mainAcctWindow.title('Sub Account')
        mainAcctApp = SubAccount(mainAcctWindow, subAcctDB)
    elif accountType == "Bank":
        mainAcctWindow.title('Bank Account')
        mainAcctApp = BankAccount(mainAcctWindow, bankAcctDB)
    #mainAcctWindow.destroy()

#SJ0201024 - Callback for monthly transaction
def monthlyTransactionCallback():
    print('Inside monthlyTransactionCallback...')
    inputDate = SelectDateDialog(mainWindow, 'Please select the date to browse the record from')
    mainWindow.wait_window(inputDate.dateDialog)
    fromDate = str(inputDate.getFromDate())
    
    #SJ3301024 - Here we form date string for next month
    year = int(fromDate[:4])
    month = int(fromDate[5:7])
    #day = int(fromDate[8:])
    day = 1
    nextMonth = month + 1
    #SJ3301024 - Disini kita check apa bulan depan mengakibatkan tahun depan
    if nextMonth > 12:
        nextMonth -= 12  #SJ3301024 - Dijadikan bulan january
        year = year + 1  #SJ3301024 - Dijadikan tahun depan
    toDate = str(year)+'-'+str(nextMonth).zfill(2)+'-'+str(day).zfill(2)
    #SJ1281024 - Now that the commencing date had been obtained, next is to decide if there are records to be displayed
    recData = sjAcctDB.complexRead("date, mainAcct, subAcct, amount, post_to, status", "date >= ? AND date < ?", (fromDate, toDate))
    totalRecords = len(recData)
    
    if totalRecords == 0:
        #print("No record found ")
        showwarning(title='No Records Found', message='No records that match your input date.')
    else:
        #SJ1111124 - Kesini berarti ada data utk di display
        #SJ0241124 - Create object untuk browsing
        browseTrans = BrowsingTransactions(recData)
        browseTrans.browsingScreenLayout()

#SJ5310323 - Create main window
mainWindow = Tk()
mainWindow.title('SJ Transaksi')
mainWindow.protocol('WM_DELETE_WINDOW', quitter_function)
#SJ3190423 - Setup Main Account SQL connection
mainAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'mainAcct', ['mainAcct', 'description'])
#app = MainAccount(mainWindow, mainAcctDB)
subAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'subAcct', ['subAcct', 'description'])
#app = SubAccount(mainWindow, subAcctDB)
bankAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'bankAcct', ['bankCode', 'bank', 'amount', 'xchangeRate', 'cadAmount'])
#app = BankAccount(mainWindow, bankAcctDB)

#bankAcctWindow = Frame(mainWindow) #, width=5000, height=3000)
#app = BankAccount(bankAcctWindow, bankAcctDB)

sjAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'sjAcct', ['indexKey', 'date', 'mainAcct', 'subAcct', 'beacon', 'amount', 'db_cr', 'post_to', 'status', 'remark'])
app = SjAccount(mainWindow, mainAcctDB, subAcctDB, bankAcctDB, sjAcctDB)
mainMenu(mainWindow)
mainloop()  #SJ5310323 - Creating long-running event loop
