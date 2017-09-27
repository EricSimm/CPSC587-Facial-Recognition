# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFace.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addPersonPage(object):
    def setupUi(self, addPersonPage):
        addPersonPage.setObjectName("addPersonPage")
        addPersonPage.resize(571, 460)
        addPersonPage.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.gridLayout = QtWidgets.QGridLayout(addPersonPage)
        self.gridLayout.setObjectName("gridLayout")
        self.continueBtn = QtWidgets.QPushButton(addPersonPage)
        self.continueBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.continueBtn.setObjectName("continueBtn")
        self.gridLayout.addWidget(self.continueBtn, 6, 0, 1, 1)
        self.backBtn = QtWidgets.QPushButton(addPersonPage)
        self.backBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 8, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(addPersonPage)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(addPersonPage)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.firstNamelbl = QtWidgets.QLabel(addPersonPage)
        self.firstNamelbl.setObjectName("firstNamelbl")
        self.gridLayout.addWidget(self.firstNamelbl, 2, 0, 1, 1)
        self.lastNameLbl = QtWidgets.QLabel(addPersonPage)
        self.lastNameLbl.setObjectName("lastNameLbl")
        self.gridLayout.addWidget(self.lastNameLbl, 4, 0, 1, 1)
        self.whatNameLbl = QtWidgets.QLabel(addPersonPage)
        self.whatNameLbl.setObjectName("whatNameLbl")
        self.gridLayout.addWidget(self.whatNameLbl, 0, 0, 1, 1)
        self.errorLbl = QtWidgets.QLabel(addPersonPage)
        self.errorLbl.setObjectName("errorLbl")
        self.gridLayout.addWidget(self.errorLbl, 5, 0, 1, 1)

        self.retranslateUi(addPersonPage)
        QtCore.QMetaObject.connectSlotsByName(addPersonPage)

    def retranslateUi(self, addPersonPage):
        _translate = QtCore.QCoreApplication.translate
        addPersonPage.setWindowTitle(_translate("addPersonPage", "AddNewFace"))
        self.continueBtn.setText(_translate("addPersonPage", "Continue"))
        self.backBtn.setText(_translate("addPersonPage", "Back"))
        self.firstNamelbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">First Name</span></p></body></html>"))
        self.lastNameLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Last Name</span></p></body></html>"))
        self.whatNameLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">What is</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">your</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Name?</span></p></body></html>"))
        self.errorLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addPersonPage = QtWidgets.QWidget()
    ui = Ui_addPersonPage()
    ui.setupUi(addPersonPage)
    addPersonPage.show()
    sys.exit(app.exec_())

