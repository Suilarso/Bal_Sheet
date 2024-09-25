#Project: SJ transaksi sehari sehari - BankAccount class
#Date: Sep 24, 24

from tkinter import *
from tkinter.messagebox import *


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



