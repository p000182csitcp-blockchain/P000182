# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Send_Message.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog


class Ui_Send_Message(object):
    def setupUi(self, Send_Message):
        Send_Message.setObjectName("Send_Message")
        Send_Message.resize(554, 618)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Send_Message.setFont(font)
        self.label_Sender_Username = QtWidgets.QLabel(Send_Message)
        self.label_Sender_Username.setGeometry(QtCore.QRect(50, 120, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Sender_Username.setFont(font)
        self.label_Sender_Username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Sender_Username.setObjectName("label_Sender_Username")
        self.comboBox_Receiver = QtWidgets.QComboBox(Send_Message)
        self.comboBox_Receiver.setGeometry(QtCore.QRect(290, 131, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Receiver.setFont(font)
        self.comboBox_Receiver.setEditable(False)
        self.comboBox_Receiver.setObjectName("comboBox_Receiver")
        self.text_Message = QtWidgets.QTextEdit(Send_Message)
        self.text_Message.setGeometry(QtCore.QRect(30, 300, 491, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.text_Message.setFont(font)
        self.text_Message.setObjectName("text_Message")
        self.pushButton_Selec_Private_Key = QtWidgets.QPushButton(Send_Message)
        self.pushButton_Selec_Private_Key.setGeometry(QtCore.QRect(30, 450, 151, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.pushButton_Selec_Private_Key.setFont(font)
        self.pushButton_Selec_Private_Key.setAutoDefault(False)
        self.pushButton_Selec_Private_Key.setDefault(False)
        self.pushButton_Selec_Private_Key.setFlat(False)
        self.pushButton_Selec_Private_Key.setObjectName("pushButton_Selec_Private_Key")
        self.label_Private_Key_Location = QtWidgets.QLabel(Send_Message)
        self.label_Private_Key_Location.setGeometry(QtCore.QRect(190, 450, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label_Private_Key_Location.setFont(font)
        self.label_Private_Key_Location.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_Private_Key_Location.setObjectName("label_Private_Key_Location")
        self.pushButton_Send = QtWidgets.QPushButton(Send_Message)
        self.pushButton_Send.setGeometry(QtCore.QRect(410, 570, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_Send.setFont(font)
        self.pushButton_Send.setObjectName("pushButton_Send")
        self.label_Choose_A_Send_Type = QtWidgets.QLabel(Send_Message)
        self.label_Choose_A_Send_Type.setGeometry(QtCore.QRect(30, 490, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Choose_A_Send_Type.setFont(font)
        self.label_Choose_A_Send_Type.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_Choose_A_Send_Type.setObjectName("label_Choose_A_Send_Type")
        self.radioButton_Encrypt = QtWidgets.QRadioButton(Send_Message)
        self.radioButton_Encrypt.setGeometry(QtCore.QRect(40, 520, 115, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioButton_Encrypt.setFont(font)
        self.radioButton_Encrypt.setObjectName("radioButton_Encrypt")
        self.radioButton_Sign = QtWidgets.QRadioButton(Send_Message)
        self.radioButton_Sign.setGeometry(QtCore.QRect(220, 520, 115, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioButton_Sign.setFont(font)
        self.radioButton_Sign.setObjectName("radioButton_Sign")
        self.radioButton_Enccrypt_And_Sign = QtWidgets.QRadioButton(Send_Message)
        self.radioButton_Enccrypt_And_Sign.setGeometry(QtCore.QRect(380, 520, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_Enccrypt_And_Sign.setFont(font)
        self.radioButton_Enccrypt_And_Sign.setObjectName(
            "radioButton_Enccrypt_And_Sign"
        )
        self.label_Sender_Icon = QtWidgets.QLabel(Send_Message)
        self.label_Sender_Icon.setGeometry(QtCore.QRect(120, 40, 91, 71))
        self.label_Sender_Icon.setStyleSheet(
            "image: url(:/res/send.png);\n" "image: url(:/icon/res/send.png);"
        )
        self.label_Sender_Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Sender_Icon.setText("")
        self.label_Sender_Icon.setObjectName("label_Sender_Icon")
        self.label_Receiver_Icon = QtWidgets.QLabel(Send_Message)
        self.label_Receiver_Icon.setGeometry(QtCore.QRect(320, 40, 71, 71))
        self.label_Receiver_Icon.setStyleSheet(
            "\n" "image: url(:/icon/res/receive.png);"
        )
        self.label_Receiver_Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Receiver_Icon.setText("")
        self.label_Receiver_Icon.setObjectName("label_Receiver_Icon")
        self.label_RPK = QtWidgets.QLabel(Send_Message)
        self.label_RPK.setGeometry(QtCore.QRect(30, 160, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_RPK.setFont(font)
        self.label_RPK.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_RPK.setObjectName("label_RPK")
        self.textEdit_Receiver_Public_Key = QtWidgets.QTextEdit(Send_Message)
        self.textEdit_Receiver_Public_Key.setGeometry(QtCore.QRect(30, 190, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textEdit_Receiver_Public_Key.setFont(font)
        self.textEdit_Receiver_Public_Key.setObjectName("textEdit_Receiver_Public_Key")
        self.label_Message = QtWidgets.QLabel(Send_Message)
        self.label_Message.setGeometry(QtCore.QRect(30, 260, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Message.setFont(font)
        self.label_Message.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_Message.setObjectName("label_Message")

        self.retranslateUi(Send_Message)
        QtCore.QMetaObject.connectSlotsByName(Send_Message)

        self.pushButton_Selec_Private_Key.clicked.connect(self.select_private_key)

    def retranslateUi(self, Send_Message):
        _translate = QtCore.QCoreApplication.translate
        Send_Message.setWindowTitle(_translate("Send_Message", "Send Message"))
        self.label_Sender_Username.setText(_translate("Send_Message", "Alice"))
        self.text_Message.setPlaceholderText(
            _translate("Send_Message", "The message you want to say")
        )
        self.pushButton_Selec_Private_Key.setText(
            _translate("Send_Message", "Select private key")
        )
        self.label_Private_Key_Location.setText(
            _translate("Send_Message", "file/private_key.pem")
        )
        self.pushButton_Send.setText(_translate("Send_Message", "Send >"))
        self.label_Choose_A_Send_Type.setText(
            _translate("Send_Message", "Choose a send type")
        )
        self.radioButton_Encrypt.setText(_translate("Send_Message", "Encrypt"))
        self.radioButton_Sign.setText(_translate("Send_Message", "Sign"))
        self.radioButton_Enccrypt_And_Sign.setText(
            _translate("Send_Message", "Encrypt and Sign")
        )
        self.label_RPK.setText(_translate("Send_Message", "Receiver's publice key"))
        self.textEdit_Receiver_Public_Key.setHtml(
            _translate(
                "Send_Message",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Arial'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.label_Message.setText(_translate("Send_Message", "Message"))

    # select and set the private key path
    def select_private_key(self):
        fname = QFileDialog.getOpenFileName(
            None,
            "Open file",
            "C:\desktop",
            "Files (*.pem)",
        )
        self.label_Private_Key_Location.setText(fname[0])

    def sendingRequest(self):
        return (
            self.comboBox_Receiver.currentText(),
            self.textEdit_Receiver_Public_Key.toPlainText(),
            self.text_Message.toPlainText(),
            self.label_Private_Key_Location.text(),
            self.radioButton_Encrypt.isChecked(),
            self.radioButton_Sign.isChecked(),
            self.radioButton_Enccrypt_And_Sign.isChecked(),
        )

    def show_info(self, info):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Sending Information")
        msg_box.setText(info)
        x = msg_box.exec_()

    def show_error(self, error):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Sending Error")
        msg_box.setText(error)
        msg_box.setIcon(QMessageBox.Critical)
        x = msg_box.exec_()


import interfaces.res_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Send_Message = QtWidgets.QWidget()
    ui = Ui_Send_Message()
    ui.setupUi(Send_Message)
    Send_Message.show()
    sys.exit(app.exec_())
