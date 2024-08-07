#Project: SJ transaksi sehari sehari
#Date: Mar 30, 23

from tkinter import *
from tkinter.messagebox import *
from tkcalendar import DateEntry  #SJ4300524 - 
from datetime import datetime  #SJ2280524
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
    #SJ4180424 - time will do all the validity check after the user click on the save button.
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
        pass

    def saveButtonCallback(self):
        #SJ1290724 - Sebelum data yg tercantum di gui layar di saved ke sjAcctDb, data dari amount field perlu di check validity nya
        
        if (self.verifySjAcctData()):
            #print("tempAmt: ", isinstance(tempAmt, (int, float)))
            #print("transDate: {0}, mainAcctOption: {1}, subAcctOption: {2}, beaconOption: {3}".format(self.date.get_date(), self.mainAcctOption.get(), self.subAcctOption.get(), self.beaconOption.get()))
            #print("amount: {0}, db_crOption: {1}, postToOption: {2}, status: {3}, remark: {4}".format(eval(self.amount.get()), self.db_crOption.get(), self.postToOption.get(), self.status.get(), self.remark.get()))
            self.sjAcctDB.saveRecords(self.date.get_date(), self.mainAcctOption.get(), self.subAcctOption.get(), self.beaconOption.get(), 
                                      eval(self.amount.get()), self.db_crOption.get(), self.postToOption.get(), self.status.get(), self.remark.get())
 
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
subAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'subAcct', ['subAcct', 'description'])
#app = SubAccount(mainWindow, subAcctDB)
bankAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'bankAcct', ['bankCode', 'bank', 'amount', 'xchangeRate', 'cadAmount'])
#app = BankAccount(mainWindow, bankAcctDB)

#bankAcctWindow = Frame(mainWindow) #, width=5000, height=3000)
#app = BankAccount(bankAcctWindow, bankAcctDB)

sjAcctDB = SetupSQLConnection('./dbase/financialDB.sqlite', 'sjAcct', ['date', 'mainAcct', 'subAcct', 'beacon', 'amount', 'db_cr', 'post_to', 'status', 'remark'])
app = SjAccount(mainWindow, mainAcctDB, subAcctDB, bankAcctDB, sjAcctDB)
mainloop()  #SJ5310323 - Creating long-running event loop
