#Project: SJ transaksi sehari sehari - SubAccount class
#Date: Sep 24, 24

from tkinter import *
from tkinter.messagebox import *


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
        self.cancelButton = Button(mainWidget, text='Cancel', command=lambda x=mainWidget: self.cancelButtonCallback(x))
        self.cancelButton.grid(row=self.cancelButtonRow, column=self.cancelButtonCol, pady=10)
        self.saveButton = Button(mainWidget, text='Save', command=lambda x=mainWidget: self.saveButtonCallback(x))
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




