# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFaceNoScale.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainPageNoScale
import exaction
import dataGeneration
import SVM

class Ui_addPersonPage(object):
        #opens up the MainPage
    def backToMainPage(self, addPersonPage):
        self.window = QtWidgets.QWidget()
        self.ui = MainPageNoScale.Ui_mainPage()
        self.ui.setupUi(self.window)
        self.window.show()
        addPersonPage.close()

    #Check if name is valid, if it is add camera
    def continueAddFaceImage(self):
        firstName = self.lineEdit.text()
        lastName = self.lineEdit_2.text()
        if not firstName or not lastName:
            self.msgLbl.setText("<font color='red'>Please enter a full name</font>")
        else:
            lock = True
            lock1 = True
            lock2 = True
            self.msgLbl.setText("<font color='red'>Processing Face</font>")
            lock = exaction.webcamScreenshot(firstName + ' ' + lastName)
            while lock:
                pass
            if not lock:
                lock1 = dataGeneration.dataGeneration()
                while lock1:
                    pass
                if not lock1:
                    lock2 = SVM.SVM()
                    while lock2:
                        pass
                    if not lock2:
                        self.msgLbl.setText("<font color='red'>Done</font>")
    
    def setupUi(self, addPersonPage):
        addPersonPage.setObjectName("addPersonPage")
        addPersonPage.resize(1280, 714)
        addPersonPage.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.continueBtn = QtWidgets.QPushButton(addPersonPage)
        self.continueBtn.setGeometry(QtCore.QRect(500, 650, 321, 24))
        self.continueBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.continueBtn.setObjectName("continueBtn")
        self.backBtn = QtWidgets.QPushButton(addPersonPage)
        self.backBtn.setGeometry(QtCore.QRect(500, 680, 321, 24))
        self.backBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.backBtn.setObjectName("backBtn")
        self.lineEdit_2 = QtWidgets.QLineEdit(addPersonPage)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 470, 381, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(addPersonPage)
        self.lineEdit.setGeometry(QtCore.QRect(470, 410, 381, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.firstNamelbl = QtWidgets.QLabel(addPersonPage)
        self.firstNamelbl.setGeometry(QtCore.QRect(620, 440, 66, 16))
        self.firstNamelbl.setObjectName("firstNamelbl")
        self.lastNameLbl = QtWidgets.QLabel(addPersonPage)
        self.lastNameLbl.setGeometry(QtCore.QRect(620, 500, 65, 16))
        self.lastNameLbl.setObjectName("lastNameLbl")
        self.whatNameLbl = QtWidgets.QLabel(addPersonPage)
        self.whatNameLbl.setGeometry(QtCore.QRect(400, 130, 511, 191))
        self.whatNameLbl.setObjectName("whatNameLbl")
        self.msgLbl = QtWidgets.QLabel(addPersonPage)
        self.msgLbl.setGeometry(QtCore.QRect(570, 520, 191, 16))
        self.msgLbl.setText("")
        self.msgLbl.setObjectName("msgLbl")
        #go back to main menu when back button is clicked
        self.backBtn.clicked.connect(lambda: self.backToMainPage(addPersonPage))
        self.continueBtn.clicked.connect(self.continueAddFaceImage)
        self.retranslateUi(addPersonPage)
        QtCore.QMetaObject.connectSlotsByName(addPersonPage)

    def retranslateUi(self, addPersonPage):
        _translate = QtCore.QCoreApplication.translate
        addPersonPage.setWindowTitle(_translate("addPersonPage", "AddNewFace"))
        self.continueBtn.setText(_translate("addPersonPage", "Continue"))
        self.backBtn.setText(_translate("addPersonPage", "Back"))
        self.firstNamelbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">First Name</span></p></body></html>"))
        self.lastNameLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Last Name</span></p></body></html>"))
        self.whatNameLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#ffffff;\">What is</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#ffffff;\">your</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#ffffff;\">Name?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addPersonPage = QtWidgets.QWidget()
    ui = Ui_addPersonPage()
    ui.setupUi(addPersonPage)
    addPersonPage.show()
    sys.exit(app.exec_())

