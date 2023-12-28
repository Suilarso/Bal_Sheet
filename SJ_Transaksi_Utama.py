#Project: SJ transaksi sehari sehari
#Date: Mar 30, 23

from tkinter import *
from tkinter.messagebox import *
import sqlite3

#SJ4300323 - This class setup Main Account data entry screen
class MainAccount:
    def __init__(self, mainWidget, mainAcctDB):
        self.mainAcctDB = mainAcctDB
        self.account = ''
        self.desc = ''
        self.mainAcct = ''
        self.description = ''
        self.mainAcctLabelRow = 1
        self.mainAcctLabelCol = 1
        self.mainAcctEntryRow = self.mainAcctLabelRow  #Row 1
        self.mainAcctEntryCol = self.mainAcctLabelCol + 1  #Col 2

        self.descriptionLabelRow = self.mainAcctLabelRow + 2  #Row 3
        self.descriptionLabelCol = 1
        self.descriptionEntryRow = self.descriptionLabelRow  #Row 3
        self.descriptionEntryCol = self.descriptionLabelCol + 1  #Col 2

        self.cancelButtonRow = self.descriptionLabelRow + 2  #Row 5
        self.cancelButtonCol = 1
        self.saveButtonRow = self.cancelButtonRow
        self.saveButtonCol = self.cancelButtonCol + 1  #Col 2
        self.setupMainAcctScreen(mainWidget)

    def setupMainAcctScreen(self, mainWidget):
        """This method is used to setup data entry screen for Main Account. It contains two fields: Main account and Description"""
        self.mainAcctLabel = Label(mainWidget, text='Main Account: ').grid(row=self.mainAcctLabelRow, column=self.mainAcctLabelCol, padx=5, pady=5)
        self.mainAcct = Entry(mainWidget)
        self.mainAcct.grid(row=self.mainAcctEntryRow, column=self.mainAcctEntryCol, padx=5, pady=5)

        self.descriptionLabel = Label(mainWidget, text='Description: ').grid(row=self.descriptionLabelRow, column=self.descriptionLabelCol, pady=5)
        self.description = Entry(mainWidget)
        self.description.grid(row=self.descriptionEntryRow, column=self.descriptionEntryCol, pady=5)

        #SJ4130423 - Cancel and Save button
        self.cancelButton = Button(text='Cancel', command=lambda x=mainWidget: self.cancelButtonCallback(x))
        self.cancelButton.grid(row=self.cancelButtonRow, column=self.cancelButtonCol, pady=10)
        self.saveButton = Button(text='Save', command=lambda x=mainWidget: self.saveButtonCallback(x))
        self.saveButton.grid(row=self.saveButtonRow, column=self.saveButtonCol)

        self.initializeMainAcctScreen(mainWidget)

    def initializeMainAcctScreen(self, mainWidget):
        self.mainAcct.delete(0, END)
        self.mainAcct.focus_set()
        self.description.delete(0, END)

    def cancelButtonCallback(self, mainWidget):
        #SJ2141123 - Left blank at the moment; think properly how and what to implement here.
        pass

    def saveButtonCallback(self, mainWidget):
        #SJ2160523 - Tasks to complete here: Verify if data keyed in already exist in mainAcct table. If it is, promgt the user
        #SJ2160523 - otherwise, pass the data captured to sql to be saved into main acct database
        #SJ4080623 - Once the data has been saved, refresh the data entry screen
        #print('MainAccount--> Main acct: {0}, Description: {1}'.format(self.mainAcct.get(), self.description.get()))
        tempAcct = self.mainAcct.get()
        retRecords = self.mainAcctDB.readRecord("mainAcct", tempAcct)
        #totalRecords = len(retRecords)
        if (len(retRecords) > 0):  #SJ1131123 - record already exist in mainAcct table
            showwarning(title="Duplicate", message=tempAcct+" already exist in mainAcct table")
        else:
            self.mainAcctDB.saveRecords(self.mainAcct.get(), self.description.get()) #SJ4280923 - Valid sttmt
            self.initializeMainAcctScreen(mainWidget) #SJ4280923 - Valid sttmt

    def __del__(self):
        print('Destructor for MainAccount class')

#SJ1260623 - This class setup GUI for sub-account entry screen
class SubAccount():
    def __init__(self, mainWidget, subAcctDB):
        #https://drive.google.com/drive/folders/1JunqyClcjsLtpMBVn6FCiqs1XTYntJWf?usp=sharing
        self.subAcctDB = subAcctDB
        #self.account = ''
        #self.desc = ''
        self.subAcct = ''
        self.description = ''
        self.subAcctLabelRow = 1
        self.subAcctLabelCol = 1
        self.subAcctEntryRow = self.subAcctLabelRow  #Row 1
        self.subAcctEntryCol = self.subAcctLabelCol + 1  #Col 2

        self.descriptionLabelRow = self.subAcctLabelRow + 2  #Row 3
        self.descriptionLabelCol = 1
        self.descriptionEntryRow = self.descriptionLabelRow  #Row 3
        self.descriptionEntryCol = self.descriptionLabelCol + 1  #Col 2

        self.cancelButtonRow = self.descriptionLabelRow + 2  #Row 5
        self.cancelButtonCol = 1
        self.saveButtonRow = self.cancelButtonRow
        self.saveButtonCol = self.cancelButtonCol + 1  #Col 2
        self.setupSubAcctScreen(mainWidget)

    def setupSubAcctScreen(self, mainWidget):
        """This method is used to setup data entry screen for Sub-Account. It contains two fields: Sub account and Description"""
        self.subAcctLabel = Label(mainWidget, text='Sub Account: ').grid(row=self.subAcctLabelRow, column=self.subAcctLabelCol, padx=5, pady=5)
        self.subAcct = Entry(mainWidget)
        self.subAcct.grid(row=self.subAcctEntryRow, column=self.subAcctEntryCol, padx=5, pady=5)

        self.descriptionLabel = Label(mainWidget, text='Description: ').grid(row=self.descriptionLabelRow, column=self.descriptionLabelCol, pady=5)
        self.description = Entry(mainWidget)
        self.description.grid(row=self.descriptionEntryRow, column=self.descriptionEntryCol, pady=5)

        #SJ3200923 - Cancel and Save button
        self.cancelButton = Button(text='Cancel', command=lambda x=mainWidget: self.cancelButtonCallback(x))
        self.cancelButton.grid(row=self.cancelButtonRow, column=self.cancelButtonCol, pady=10)
        self.saveButton = Button(text='Save', command=lambda x=mainWidget: self.saveButtonCallback(x))
        self.saveButton.grid(row=self.saveButtonRow, column=self.saveButtonCol)

        self.initializeSubAcctScreen(mainWidget)

    def initializeSubAcctScreen(self, mainWidget):
        self.subAcct.delete(0, END)
        self.subAcct.focus_set()
        self.description.delete(0, END)

    def cancelButtonCallback(self, mainWidget):
        pass

    def saveButtonCallback(self, mainWidget):
        #SJ3200923 - Tasks to complete here: pass the data captured to sql to be saved into sub acct database
        #SJ3200923 - Once the data has been saved, refresh the data entry screen
        #print('MainAccount--> Main acct: {0}, Description: {1}'.format(self.mainAcct.get(), self.description.get()))
        tempSubAcct = self.subAcct.get()
        retRecords = self.subAcctDB.readRecord("SubAcct", tempSubAcct)
        #totalRecords = len(retRecords)
        if (len(retRecords) > 0):  #SJ1131123 - record already exist in mainAcct table
            showwarning(title="Duplicate", message=tempSubAcct+" already exist in subAcct table")
        else:
            self.subAcctDB.saveRecords(self.subAcct.get(), self.description.get())  #SJ4280923 - Valid code, block for testing other sttmt
            self.initializeSubAcctScreen(mainWidget)  #SJ4280923 - Valid code, block for testing other sttmt

    def __del__(self):
        print('Destructor for SubAccount class')

#SJ1181223 - This class setup GUI for bank account entry screen
class BankAccount():
    def __init__(self, mainWidget, bankAcctDB):
        self.bankAcctDB = bankAcctDB
        #self.account = ''
        #self.desc = ''
        self.bankCode = ''
        self.bankName = ''
        self.amount = 0.0
        self.exchangeRate = 0.0
        self.cadAmount = 0.0  #SJ6231223 - Is this var needed at all
        #SJ3271223 - Bank code entry field
        self.bankCodeLabelRow = 1
        self.bankCodeLabelCol = 1
        self.bankCodeEntryRow = self.bankCodeLabelRow  #Row 1
        self.bankCodeEntryCol = self.bankCodeLabelCol + 1  #Col 2
        #SJ3271223 - Bank name entry field
        self.bankNameLabelRow = self.bankCodeLabelRow
        self.bankNameLabelCol = self.bankCodeEntryCol + 1  #Col 3
        self.bankNameeEntryRow = self.bankNameLabelRow  #Row 1
        self.bankNameEntryCol = self.bankNameLabelCol + 1  #Col 4
#SJ6231223 - SJSTOP_HERE
        self.descriptionLabelRow = self.subAcctLabelRow + 2  #Row 3
        self.descriptionLabelCol = 1
        self.descriptionEntryRow = self.descriptionLabelRow  #Row 3
        self.descriptionEntryCol = self.descriptionLabelCol + 1  #Col 2

        self.cancelButtonRow = self.descriptionLabelRow + 2  #Row 5
        self.cancelButtonCol = 1
        self.saveButtonRow = self.cancelButtonRow
        self.saveButtonCol = self.cancelButtonCol + 1  #Col 2
        self.setupSubAcctScreen(mainWidget)
        pass

    def __del__(self):
        print('Destructor for BankAccount class')


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
        #curCursor.execute('SELECT workOrder, customerName, dateReceived FROM werChecklist WHERE dateReceived >= ? AND dateReceived < ?', (fromDate, toDate))
        #totalRecords = len(recData)

        #curCursor.execute('SELECT workOrder FROM werChecklist WHERE workOrder = ? LIMIT 1', (self.workOrder, ))
        #count = curCursor.fetchone()
        #if count != None:
            #count = curCursor.fetchone()[0]
        #    showwarning(title='Duplicate WOP', message='It seems '+self.workOrder+' had been used.')

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
        print('Destructor for SetupSQLConnection class')

def quitter_function():
    print('quitter_function: Closing sql connection and destroy root object...')
    #conn.close()  #SJ5310323 - Close database connection, to be un-remarked
    mainWindow.destroy()

#SJ5310323 - Create main window
mainWindow = Tk()
mainWindow.title('SJ Transaksi')
mainWindow.protocol('WM_DELETE_WINDOW', quitter_function)
#SJ3190423 - Setup Main Account SQL connection
mainAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'mainAcct', ['mainAcct', 'description'])
#app = MainAccount(mainWindow, mainAcctDB)
subAcctDB =  SetupSQLConnection('./dbase/financialDB.sqlite', 'subAcct', ['subAcct', 'description'])
#app = MainAccount(mainWindow, mainAcctDB)
app = SubAccount(mainWindow, subAcctDB)
mainloop()  #SJ5310323 - Creating long-running event loop
