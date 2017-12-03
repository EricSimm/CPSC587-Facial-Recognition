# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPageNoScale.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import CameraRecognition
import AddFaceNoScale
import faceRecognition
import os
import AboutPage2

def find(name, path):
    for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

class Ui_mainPage(object):
    #go to instruction/about page
    def toAboutPage(self, mainPage):
        self.window = QtWidgets.QWidget()
        self.ui = AboutPage2.Ui_aboutPage()
        self.ui.setupUi(self.window)
        self.window.show()
    
    #go to facial recognition page
    def toRecognition(self, mainPage):
        self.window = QtWidgets.QWidget()
        self.ui = CameraRecognition.Ui_camRecognitionPage()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def recognitionCam(self):
        faceRecognition.faceRecognition()
        
        
    #go to AddFace page
    def toAddFace(self, mainPage):
        self.window = QtWidgets.QWidget()
        self.ui = AddFaceNoScale.Ui_addPersonPage()
        self.ui.setupUi(self.window)
        self.window.show()
        mainPage.close()


    
    def setupUi(self, mainPage):
        mainPage.setObjectName("mainPage")
        mainPage.resize(1280, 800)
        mainPage.setAutoFillBackground(False)
        mainPage.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.addFaceBtn = QtWidgets.QPushButton(mainPage)
        self.addFaceBtn.setGeometry(QtCore.QRect(530, 620, 201, 41))
        self.addFaceBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.addFaceBtn.setObjectName("addFaceBtn")
        self.label = QtWidgets.QLabel(mainPage)
        self.label.setGeometry(QtCore.QRect(470, 60, 371, 271))
        self.label.setObjectName("label")
        self.aboutBtn = QtWidgets.QPushButton(mainPage)
        self.aboutBtn.setGeometry(QtCore.QRect(530, 690, 201, 41))
        self.aboutBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.aboutBtn.setObjectName("aboutBtn")
        self.startRecBtn = QtWidgets.QPushButton(mainPage)
        self.startRecBtn.setGeometry(QtCore.QRect(530, 550, 201, 41))
        self.startRecBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.startRecBtn.setObjectName("startRecBtn")
        self.imageLbl = QtWidgets.QLabel(mainPage)
        self.imageLbl.setGeometry(QtCore.QRect(490, 320, 281, 211))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLbl.setText("")
        self.imageLbl.setPixmap(QtGui.QPixmap("../src/smileimage.png"))
        self.imageLbl.setObjectName("imageLbl")
        self.addFaceBtn.clicked.connect(lambda: self.toAddFace(mainPage))
        self.aboutBtn.clicked.connect(lambda: self.toAboutPage(mainPage))
        self.startRecBtn.clicked.connect(self.recognitionCam)
        self.retranslateUi(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)
        

    def retranslateUi(self, mainPage):
        _translate = QtCore.QCoreApplication.translate
        mainPage.setWindowTitle(_translate("mainPage", "MainPage"))
        self.addFaceBtn.setText(_translate("mainPage", "Add Face"))
        self.label.setText(_translate("mainPage", "<html><head/><body><p><span style=\" font-size:144pt; color:#ffffff;\">Smile</span></p></body></html>"))
        self.aboutBtn.setText(_translate("mainPage", "Instrucitons"))
        self.startRecBtn.setText(_translate("mainPage", "Start Recognition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QWidget()
    ui = Ui_mainPage()
    ui.setupUi(mainPage)
    mainPage.show()
    sys.exit(app.exec_())

