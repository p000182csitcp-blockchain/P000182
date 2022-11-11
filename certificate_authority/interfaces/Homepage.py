# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import interfaces.res_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
import os
from MongoDB.UserFactory import *


class Ui_Homepage(object):
    def setupUi(self, Homepage):
        Homepage.setObjectName("Homepage")
        Homepage.resize(573, 516)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Homepage.sizePolicy().hasHeightForWidth())
        Homepage.setSizePolicy(sizePolicy)
        self.label_Photo = QtWidgets.QLabel(Homepage)
        self.label_Photo.setGeometry(QtCore.QRect(140, 60, 81, 81))
        self.label_Photo.setMouseTracking(False)
        self.label_Photo.setAutoFillBackground(False)
        self.label_Photo.setStyleSheet("image: url(:/icon/res/user.png);")
        self.label_Photo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Photo.setText("")
        self.label_Photo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Photo.setObjectName("label_Photo")
        self.pushButton_Update_photo = QtWidgets.QPushButton(Homepage)
        self.pushButton_Update_photo.setGeometry(
            QtCore.QRect(230, 110, 150, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Update_photo.setFont(font)
        self.pushButton_Update_photo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_Update_photo.setStyleSheet("color: rgb(99, 148, 255);")
        self.pushButton_Update_photo.setFlat(True)
        self.pushButton_Update_photo.setObjectName("pushButton_Update_photo")
        self.label_Username = QtWidgets.QLabel(Homepage)
        self.label_Username.setGeometry(QtCore.QRect(230, 70, 230, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_Username.setFont(font)
        self.label_Username.setObjectName("label_Username")
        self.pushButton_Log_Out = QtWidgets.QPushButton(Homepage)
        self.pushButton_Log_Out.setGeometry(QtCore.QRect(360, 20, 100, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Log_Out.setFont(font)
        self.pushButton_Log_Out.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(0, 85, 255);"
        )
        self.pushButton_Log_Out.setFlat(False)
        self.pushButton_Log_Out.setObjectName("pushButton_Log_Out")
        self.pushButton_Download_Key_Pairs = QtWidgets.QPushButton(Homepage)
        self.pushButton_Download_Key_Pairs.setGeometry(
            QtCore.QRect(210, 150, 200, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Download_Key_Pairs.setFont(font)
        self.pushButton_Download_Key_Pairs.setStyleSheet(
            "color: rgb(99, 148, 255);")
        self.pushButton_Download_Key_Pairs.setFlat(False)
        self.pushButton_Download_Key_Pairs.setObjectName(
            "pushButton_Download_Key_Pairs"
        )
        self.label_Send_File_background = QtWidgets.QLabel(Homepage)
        self.label_Send_File_background.setGeometry(
            QtCore.QRect(140, 200, 131, 121))
        self.label_Send_File_background.setStyleSheet(
            "background-color: rgb(147, 147, 255);"
        )
        self.label_Send_File_background.setText("")
        self.label_Send_File_background.setObjectName(
            "label_Send_File_background")
        self.label_Send_File_Icon = QtWidgets.QLabel(Homepage)
        self.label_Send_File_Icon.setGeometry(QtCore.QRect(170, 220, 71, 61))
        self.label_Send_File_Icon.setStyleSheet(
            "image: url(:/icon/res/send_file.png);")
        self.label_Send_File_Icon.setText("")
        self.label_Send_File_Icon.setObjectName("label_Send_File_Icon")
        self.pushButton_Send_File = QtWidgets.QPushButton(Homepage)
        self.pushButton_Send_File.setGeometry(QtCore.QRect(140, 290, 131, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Send_File.setFont(font)
        self.pushButton_Send_File.setStyleSheet("")
        self.pushButton_Send_File.setFlat(True)
        self.pushButton_Send_File.setObjectName("pushButton_Send_File")
        self.label_Send_Message_background = QtWidgets.QLabel(Homepage)
        self.label_Send_Message_background.setGeometry(
            QtCore.QRect(290, 200, 131, 121))
        self.label_Send_Message_background.setStyleSheet(
            "background-color: rgb(198, 226, 255);"
        )
        self.label_Send_Message_background.setText("")
        self.label_Send_Message_background.setObjectName(
            "label_Send_Message_background"
        )
        self.label_Send_Message_Icon = QtWidgets.QLabel(Homepage)
        self.label_Send_Message_Icon.setGeometry(
            QtCore.QRect(320, 220, 71, 61))
        self.label_Send_Message_Icon.setStyleSheet(
            "image: url(:/icon/res/send_message.png);"
        )
        self.label_Send_Message_Icon.setText("")
        self.label_Send_Message_Icon.setObjectName("label_Send_Message_Icon")
        self.pushButton_Send_Message = QtWidgets.QPushButton(Homepage)
        self.pushButton_Send_Message.setGeometry(
            QtCore.QRect(290, 290, 131, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(10)
        self.pushButton_Send_Message.setFont(font)
        self.pushButton_Send_Message.setStyleSheet("")
        self.pushButton_Send_Message.setFlat(True)
        self.pushButton_Send_Message.setObjectName("pushButton_Send_Message")
        self.label_Check_Message_background = QtWidgets.QLabel(Homepage)
        self.label_Check_Message_background.setGeometry(
            QtCore.QRect(140, 330, 281, 131)
        )
        self.label_Check_Message_background.setStyleSheet(
            "background-color: rgb(255, 191, 127);"
        )
        self.label_Check_Message_background.setText("")
        self.label_Check_Message_background.setObjectName(
            "label_Check_Message_background"
        )
        self.label_Check_Message_Icon = QtWidgets.QLabel(Homepage)
        self.label_Check_Message_Icon.setGeometry(
            QtCore.QRect(240, 350, 71, 71))
        self.label_Check_Message_Icon.setStyleSheet(
            "image: url(:/icon/res/message.png);"
        )
        self.label_Check_Message_Icon.setText("")
        self.label_Check_Message_Icon.setObjectName("label_Check_Message_Icon")
        self.pushButton_Check_Message = QtWidgets.QPushButton(Homepage)
        self.pushButton_Check_Message.setGeometry(
            QtCore.QRect(140, 420, 281, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Check_Message.setFont(font)
        self.pushButton_Check_Message.setStyleSheet("")
        self.pushButton_Check_Message.setFlat(True)
        self.pushButton_Check_Message.setObjectName("pushButton_Check_Message")

        self.retranslateUi(Homepage)
        QtCore.QMetaObject.connectSlotsByName(Homepage)

        self.pushButton_Download_Key_Pairs.clicked.connect(
            self.download_private_key)

    def retranslateUi(self, Homepage):
        _translate = QtCore.QCoreApplication.translate
        Homepage.setWindowTitle(_translate("Homepage", "Homepage"))
        self.pushButton_Update_photo.setText(
            _translate("Homepage", "Update photo"))
        self.label_Username.setText(_translate("Homepage", "1234567890"))
        self.pushButton_Log_Out.setText(_translate("Homepage", "Log Out"))
        self.pushButton_Download_Key_Pairs.setText(
            _translate("Homepage", "Download key pairs")
        )
        self.pushButton_Send_File.setText(
            _translate("Homepage", "Send a file"))
        self.pushButton_Send_Message.setText(
            _translate("Homepage", "Send a message"))
        self.pushButton_Check_Message.setText(
            _translate("Homepage", "Check messages and files")
        )

    def download_private_key(self):
        response = QFileDialog.getExistingDirectory(
            None, caption="Select a folder")
        file_name = "my_private_key.pem"
        fname = response + "/" + file_name
        with open("file/private_key.pem", "rb") as fr:
            private_key = fr.read()
        with open(fname, "wb") as fp:
            fp.write(private_key)

        # print("fname:", fname)
        # update private_key_location on B
        UserFactory().update_private_key_location(fname, self.label_Username.text())

        # show succ info
        self.show_info("Your private key file has been downloaded.")

    def updatePhotoRequest(self):
        fname = QFileDialog.getOpenFileName(
            None,
            "Open file",
            "C:",
            "Images (*.png, *.xmp *.jpg)",
        )
        return fname[0]

    def show_info(self, info):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Download Information")
        msg_box.setText(info)
        x = msg_box.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Homepage = QtWidgets.QWidget()
    ui = Ui_Homepage()
    ui.setupUi(Homepage)
    Homepage.show()
    sys.exit(app.exec_())
