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
        self.bankAcctWidget = mainWidget
        self.bankAcctDB = bankAcctDB
        #self.account = ''
        #self.desc = ''
        self.currentField = ''
        self.bankCode = ''
        self.bankName = ''
        self.amount = 0.0
        self.exchangeRate = 0.0
        self.cadAmount = 0.0  #SJ6231223 - Is this var needed at all

        #SJ3271223 - Bank code entry field coordinate - row 1 col 1, 2
        self.bankCodeLabelRow = 1
        self.bankCodeLabelCol = 1
        self.bankCodeEntryRow = self.bankCodeLabelRow  #Row 1
        self.bankCodeEntryCol = self.bankCodeLabelCol + 1  #Col 2
        #SJ3271223 - Bank name entry field coordinate - row 1 col 4, 5
        self.bankNameLabelRow = self.bankCodeLabelRow
        self.bankNameLabelCol = self.bankCodeEntryCol + 2  #Col 4
        self.bankNameEntryRow = self.bankNameLabelRow  #Row 1
        self.bankNameEntryCol = self.bankNameLabelCol + 1  #Col 5

        #SJ4281223 - Amount entry field coordinate - row 3 col 1, 2
        self.amountLabelRow = self.bankCodeLabelRow + 2  #Row 3
        self.amountLabelCol = 1
        self.amountEntryRow = self.amountLabelRow  #Row 3
        self.amountEntryCol = self.amountLabelCol + 1  #Col 2
        #SJ4281223 - Exchange rate entry field coordinate - row 3 col 4, 5
        self.exchangeRateLabelRow = self.amountLabelRow  #Row 3
        self.exchangeRateLabelCol = self.amountEntryCol + 2  #Col 4
        self.exchangeRateEntryRow = self.exchangeRateLabelRow  #Row 3
        self.exchangeRateEntryCol = self.exchangeRateLabelCol + 1 #Col 5

        #SJ3030124 - Cancel and Save Button - row 5
        self.cancelButtonRow = self.exchangeRateLabelRow + 2  #Row 5
        self.cancelButtonCol = 1
        self.saveButtonRow = self.cancelButtonRow
        self.saveButtonCol = self.cancelButtonCol + 1  #Col 2
        self.setupBankAcctScreen(self.bankAcctWidget)

    def setupBankAcctScreen(self, mainWidget):
        """This method is used to setup data entry screen for Bank Account. It contains four fields: Bank code, Bank name, Amount,
           and Exchange rate."""

        #SJ4040124 - Bank code
        self.bankcodeLabel = Label(mainWidget, text='Bank Code: ').grid(row=self.bankCodeLabelRow, column=self.bankCodeLabelCol, padx=5, pady=5)
        self.bankCode = Entry(mainWidget)
        self.bankCode.grid(row=self.bankCodeEntryRow, column=self.bankCodeEntryCol, padx=5, pady=5)

        #SJ4040124 - Bank name
        self.bankNameLabel = Label(mainWidget, text='Description: ').grid(row=self.bankNameLabelRow, column=self.bankNameLabelCol, pady=5)
        self.bankName = Entry(mainWidget)
        self.bankName.grid(row=self.bankNameEntryRow, column=self.bankNameEntryCol, pady=5)

        #SJ4040124 - Amount
        #self.amount = 0.0
        self.amountLabel = Label(mainWidget, text='Amount: ').grid(row=self.amountLabelRow, column=self.amountLabelCol)
        self.amount = Entry(mainWidget)
        #self.amount.insert(0, '1')
        self.amount.grid(row=self.amountEntryRow, column=self.amountEntryCol)

        #SJ3070224 - Exchange rate
        self.exchangeRateLabel = Label(mainWidget, text='Exchange rate: ').grid(row=self.exchangeRateLabelRow, column=self.exchangeRateLabelCol)
        self.exchangeRate = Entry(mainWidget)
        #self.exchangeRate.insert(0, '1')
        self.exchangeRate.grid(row=self.exchangeRateEntryRow, column=self.exchangeRateEntryCol)

        self.cadAmount = 0.0

        #SJ3070224 - Cancel and Save button
        self.cancelButton = Button(text='Cancel', command=lambda x=mainWidget: self.cancelButtonCallback(x))
        self.cancelButton.grid(row=self.cancelButtonRow, column=self.cancelButtonCol, pady=10)
        self.saveButton = Button(text='Save', command=lambda x=mainWidget: self.saveButtonCallback(x))
        self.saveButton.grid(row=self.saveButtonRow, column=self.saveButtonCol)

        #mainWidget.bind("<Button-1>", self.leftButtonReleasedCallback)
        #mainWidget.bind("<ButtonRelease-1>", self.leftButtonReleasedCallback)

        self.initializeBankAcctScreen(mainWidget)

    def initializeBankAcctScreen(self, mainWidget):
        self.bankCode.delete(0, END)
        self.bankCode.focus_set()
        self.currentField = 1
        self.bankName.delete(0, END)
        self.amount.delete(0, END)
        self.exchangeRate.delete(0, END)
        self.exchangeRate.insert(0, '1')

    #SJ4180424 - Here we check for possible duplicate bank account record, and also for valid float
    #SJ4180424 - data is being keyed in.
    def verifyBankAcctData(self, mainWidget):
        numOfField = 4
        fieldBeingVerified = 1
        returnFlag = False
        while (fieldBeingVerified <= numOfField):
            #SJ1220424 - Examine bankCode field; two test to be carried out: check empty field
            #SJ1220424 - and check for duplicate record
            if fieldBeingVerified == 1:
                tempBankCode = self.bankCode.get().strip()
                if (len(tempBankCode) > 0):
                    #SJ5190424 - Bank code is not blank, so proceed to check for duplicate record
                    retRecords = self.bankAcctDB.readRecord("bankCode", tempBankCode)
                    if (len(retRecords) > 0):  #SJ5190424 - record already exist in bankAcctDB table
                        showwarning(title="Duplicate", message=tempBankCode+" already exist in bankAcct table")
                        self.bankCode.focus_set()
                        break
                else:
                    #SJ1220424 - bankCode field is blank
                    showerror(title="Mandatory Field", message="Bank code cannot be blank")
                    self.bankCode.focus_set()
                    break

                fieldBeingVerified += 1

            #SJ1220424 - Examine bankName field; just need to examine for empty field
            elif fieldBeingVerified == 2:
                tempBankName = self.bankName.get().strip()
                if (len(tempBankName) == 0):
                    showerror(title="Mandatory Field", message="Bank name cannot be blank")
                    self.bankName.focus_set()
                    break

                fieldBeingVerified += 1

            #SJ2230424 - Examine the input to amount field is indeed convertible to real number
            elif fieldBeingVerified == 3:
                tmpAmount = self.amount.get().strip()
                if (not (tmpAmount.isdigit())):
                    showerror(title="Invalid Input", message="Expect real number")
                    self.amount.focus_set()
                    break

                fieldBeingVerified += 1

            #SJ2230424 - Examine the input to exchangeRate field is indeed convertible to real number
            elif fieldBeingVerified == 4:
                tmpExchangeRate = self.exchangeRate.get().strip()
                if (not (tmpExchangeRate.isdigit())):
                    showerror(title="Invalid Input", message="Expect real number")
                    self.exchangeRate.focus_set()
                    break

                fieldBeingVerified += 1
            #else:
                print('verifyBankAcctData: All input data are valid')
                returnFlag = True
                #pass

        return returnFlag

    def cancelButtonCallback(self, mainWidget):
        #SJ1120224 - Here we need to re-initilize date entry screen.
        pass

    def saveButtonCallback(self, mainWidget):
        if (self.verifyBankAcctData(mainWidget)):
            #self.cadAmount = 0.0
            tempAmount = eval(self.amount.get())
            tempExchangeRate = eval(self.exchangeRate.get())
            tempCADAmount = tempAmount * tempExchangeRate
            print('bank code, bank name, temp amnt, temp exchange rate, temp cad amt: ', self.bankCode.get(), self.bankName.get(), tempAmount, tempExchangeRate, tempCADAmount)
            self.bankAcctDB.saveRecords(self.bankCode.get(), self.bankName.get(), tempAmount, tempExchangeRate, tempCADAmount)
            self.initializeBankAcctScreen(mainWidget)

    #SJ4180424 - This method is meant to warn user whenever a mandatory is left blank when moving
    #SJ$180424 - from one mandatory to another field, but it turns out that the implementation is
    #SJ4180424 - not straight forward for entry screen with more than one mandatory field. As such,
    #SJ4180424 - will abandon this idea for now, may re-visit this idea in the future. In the mean
    #SJ4180424 - will do all the validity check after the user click on the save button.
    def leftButtonReleasedCallback(self, event):
        childList = str(self.bankAcctWidget.winfo_children()[0].focus_get())
        ndx = strLength = len(childList)
        while ndx > 0:
            if (childList[ndx-1] in '0123456789'):
                ndx -= 1
            else:
                break
        sliceAmt = ndx - strLength
        clickedField = 1 if (sliceAmt == 0) else int(childList[sliceAmt:])
        #SJ2160424 - Here we check for mandatory field being skipped without keying in any data
        if (self.currentField != clickedField):  #SJ2160424 - jump to other fields
            if (self.currentField == 1):
                self.currentField = clickedField
                tempBankCode = self.bankCode.get().strip()
                if (len(tempBankCode) == 0):
                    showerror(title="Mandatory Field", message="Bank code cannot be blank.")
                    self.bankCode.focus_set()
                    self.currentField = 1
            elif (self.currentField == 2):
                self.currentField = clickedField
                tempBankName = self.bankName.get().strip()
                if (len(tempBankName) == 0):
                    showerror(title="Mandatory Field", message="Bank name cannot be blank.")
                    self.bankName.focus_set()
                    self.currentField = 2
            else:
                self.currentField = clickedField
        print('Current field: ', self.currentField)

    def __del__(self):
        print('Destructor for BankAccount class')
        print('Unbinding button release 1')
        #self.bankAcctWidget.unbind("<Button-1>")
        #self.bankAcctWidget.unbind("<ButtonRelease-1>")


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

        #curCursor.execute('SELECT workOrder FROM xxxTableName WHERE workOrder = ? LIMIT 1', (self.workOrder, ))
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
        print('Destructor for SetupSQLConnection class: ', self.tableName)

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
#app = SubAccount(mainWindow, subAcctDB)
bankAcctDB =  SetupSQLConnection('./dbase/financialDB.sqlite', 'bankAcct', ['bankCode', 'bank', 'amount', 'xchangeRate', 'cadAmount'])
#bankAcctWindow = Frame(mainWindow) #, width=5000, height=3000)
#app = BankAccount(bankAcctWindow, bankAcctDB)
app = BankAccount(mainWindow, bankAcctDB)
mainloop()  #SJ5310323 - Creating long-running event loop
