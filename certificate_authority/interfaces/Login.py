# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(593, 474)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        Login.setFont(font)
        Login.setStyleSheet("")
        self.label_Login = QtWidgets.QLabel(Login)
        self.label_Login.setGeometry(QtCore.QRect(60, 20, 471, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_Login.setFont(font)
        self.label_Login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Login.setObjectName("label_Login")
        self.label_Username = QtWidgets.QLabel(Login)
        self.label_Username.setGeometry(QtCore.QRect(60, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_Username.setFont(font)
        self.label_Username.setObjectName("label_Username")
        self.label_Password = QtWidgets.QLabel(Login)
        self.label_Password.setGeometry(QtCore.QRect(60, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.text_Username = QtWidgets.QTextEdit(Login)
        self.text_Username.setGeometry(QtCore.QRect(60, 140, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.text_Username.setFont(font)
        self.text_Username.setObjectName("text_Username")
        self.text_Password = QtWidgets.QTextEdit(Login)
        self.text_Password.setGeometry(QtCore.QRect(60, 240, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.text_Password.setFont(font)
        self.text_Password.setObjectName("text_Password")
        self.pushButton_Login = QtWidgets.QPushButton(Login)
        self.pushButton_Login.setGeometry(QtCore.QRect(60, 340, 471, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(0, 85, 255);"
        )
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(60, 420, 271, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_4.setObjectName("label_4")
        self.pushButton_register = QtWidgets.QPushButton(Login)
        self.pushButton_register.setGeometry(QtCore.QRect(330, 420, 71, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_register.setFont(font)
        self.pushButton_register.setStyleSheet("color: rgb(0, 85, 255);")
        self.pushButton_register.setFlat(True)
        self.pushButton_register.setObjectName("pushButton_register")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_Login.setText(_translate("Login", "Login"))
        self.label_Username.setText(_translate("Login", "Username"))
        self.label_Password.setText(_translate("Login", "Password"))
        self.text_Password.setHtml(
            _translate(
                "Login",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Arial'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'微软雅黑';\"><br /></p></body></html>",
            )
        )
        self.pushButton_Login.setText(_translate("Login", "Login"))
        self.label_4.setText(_translate("Login", "Don't have an account? "))
        self.pushButton_register.setText(_translate("Login", "Register"))

    def loginRequest(self):
        return self.text_Username.toPlainText(), self.text_Password.toPlainText()

    def show_error(self, error):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Login Warning")
        msg_box.setText(error)
        msg_box.setIcon(QMessageBox.Critical)
        x = msg_box.exec_()

    def reset_input(self):
        self.text_Username.setText("")
        self.text_Password.setText("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
