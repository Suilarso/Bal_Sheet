#Project: SJ transaksi sehari sehari - MainAccount class
#Date: Sep 24, 24

from tkinter import *
from tkinter.messagebox import *


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



