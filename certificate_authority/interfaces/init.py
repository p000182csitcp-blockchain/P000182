from PyQt5 import QtCore, QtGui, QtWidgets
from interfaces.Login import Ui_Login
from interfaces.Sign_Up import Ui_Sign_Up
from interfaces.Homepage import Ui_Homepage
from interfaces.Send_Message import Ui_Send_Message
from interfaces.Check_Message import Ui_Check_Message
from interfaces.Send_File import Ui_Send_File
from scripts.crypto import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from MongoDB.UserFactory import *
from MongoDB.User import *
from scripts.deploy import create_certificate
from deployment.Record import *
from PyQt5.QtCore import QTimer
import time


class Init:
    def __init__(self) -> None:
        self._user = None
        self._user_factory = UserFactory()
        self._m_selected = None

        self._ui_login = None
        self._ui_signUp = None
        self._ui_homePage = None
        self._ui_sendMsg = None
        self._ui_checkMsg = None
        self._ui_sendFile = None

        self._window_login = None
        self._window_signUp = None
        self._window_homePage = None
        self._window_sendMsg = None
        self._window_checkMsg = None
        self._window_sendFile = None

        self._prev_msg_count = 0

    # refresh pages every 3 sec
    def refreshPages(self):
        self.refreshTimer()

        username = self._user.get_username()
        self._user = self._user_factory.check_user_by_username(username)
        # get db msg list reatime
        db_msg_list = self._user.get_message()
        db_msg_count = len(db_msg_list)

        # if updated, refresh pages
        if db_msg_count != self._prev_msg_count:
            # update prev msg count
            self._prev_msg_count = db_msg_count
            # self.refreshSendMsg()
            # self.refreshSendFile()
            self.refreshCheckMsg()

    def refreshTimer(self):
        # Repeating timer, calls random_pick over and over
        self.picktimer = QTimer()
        self.picktimer.setInterval(500)
        self.picktimer.timeout.connect(self.refreshPages)
        self.picktimer.start()

    def openLogin(self):
        self._window_login = QMainWindow()
        self._ui_login = Ui_Login()
        self._ui_login.setupUi(self._window_login)

        # Login to Sign up button event
        self._ui_login.pushButton_register.clicked.connect(
            lambda: {self.openSignUp(), self.closeLogin()}
        )

        # Login button event
        self._ui_login.pushButton_Login.clicked.connect(lambda: {self.login()})

        self._window_login.show()

    def openSignUp(self):
        self._window_signUp = QMainWindow()
        self._ui_signUp = Ui_Sign_Up()
        self._ui_signUp.setupUi(self._window_signUp)

        # Sign up to Login button event
        self._ui_signUp.pushButton_Login.clicked.connect(
            lambda: {self.openLogin(), self.closeSignUp()}
        )

        # Signup button event
        self._ui_signUp.pushButton_Sign_Up.clicked.connect(
            lambda: {self.signUp()})

        self._window_signUp.show()

    def openHomePage(self):
        self._window_homePage = QMainWindow()
        self._ui_homePage = Ui_Homepage()
        self._ui_homePage.setupUi(self._window_homePage)

        # Home page update photo
        self._ui_homePage.pushButton_Update_photo.clicked.connect(
            lambda: {self.updatePhoto()}
        )

        # Home page go to send message page
        self._ui_homePage.pushButton_Send_Message.clicked.connect(
            lambda: {self.openSendMsg(), self.refreshSendMsg()}
        )

        # Home page go to send file page
        self._ui_homePage.pushButton_Send_File.clicked.connect(
            lambda: {self.openSendFile(), self.refreshSendFile()}
        )

        # Home page go to message list page
        self._ui_homePage.pushButton_Check_Message.clicked.connect(
            lambda: {
                self.openCheckMsg(),
                self.refreshCheckMsg(),
                self.refreshPages(),
            }
        )

        # Home page log out
        self._ui_homePage.pushButton_Log_Out.clicked.connect(
            lambda: {
                self.openLogin(),
                self.closeSendFile(),
                self.closeSendMsg(),
                self.closeHomePage(),
            }
        )

        self._window_homePage.show()

    def openSendFile(self):
        self._window_sendFile = QMainWindow()
        self._ui_sendFile = Ui_Send_File()
        self._ui_sendFile.setupUi(self._window_sendFile)

        # send file page send button event
        self._ui_sendFile.pushButton_Send.clicked.connect(
            lambda: {self.sendFile()})

        self._window_sendFile.show()

    def openSendMsg(self):
        self._window_sendMsg = QMainWindow()
        self._ui_sendMsg = Ui_Send_Message()
        self._ui_sendMsg.setupUi(self._window_sendMsg)

        # send message page send button event
        self._ui_sendMsg.pushButton_Send.clicked.connect(
            lambda: {self.sendMessage()})

        self._window_sendMsg.show()

    def openCheckMsg(self):
        self._window_checkMsg = QMainWindow()
        self._ui_checkMsg = Ui_Check_Message()
        self._ui_checkMsg.setupUi(self._window_checkMsg)

        self._ui_checkMsg.pushButton_Decrypt.clicked.connect(
            lambda: {self.decrypt()})
        self._ui_checkMsg.pushButton_Validate.clicked.connect(
            lambda: {self.verify()})
        self._ui_checkMsg.pushButton_Download_The_File.clicked.connect(
            lambda: {self.downloadFile()}
        )

        self._window_checkMsg.show()

    def closeLogin(self):
        self._ui_login = None
        if self._window_login != None:
            self._window_login.close()
            self._window_login = None

    def closeSignUp(self):
        self._ui_signUp = None
        if self._window_signUp != None:
            self._window_signUp.close()
            self._window_signUp = None

    def closeHomePage(self):
        self._ui_homePage = None
        if self._window_homePage != None:
            self._window_homePage.close()
            self._window_homePage = None

    def closeSendMsg(self):
        self._ui_sendMsg = None
        if self._window_sendMsg != None:
            self._window_sendMsg.close()
            self._window_sendMsg = None

    def closeSendFile(self):
        self._ui_sendFile = None
        if self._window_sendFile != None:
            self._window_sendFile.close()
            self._window_sendFile = None

    def closeCheckMsg(self):
        self._ui_checkMsg = None
        if self._window_checkMsg != None:
            self._window_checkMsg.close()
            self._window_checkMsg = None

    # get login request
    def getLoginRequest(self):
        return self._ui_login.loginRequest()

    # get sgin up request
    def getSignUpRequest(self):
        return self._ui_signUp.signUpRequest()

    def getUpdatePhotoRequest(self):
        return self._ui_homePage.updatePhotoRequest()

    def getSendMsgRequest(self):
        return self._ui_sendMsg.sendingRequest()

    def getSendFileRequest(self):
        return self._ui_sendFile.sendingRequest()

    def start_ui(self):
        app = QApplication([])
        # open login page at start
        self.openLogin()
        sys.exit(app.exec_())

    def login(self):
        user_name, password = self.getLoginRequest()
        # login db
        self._user = self._user_factory.check_user(user_name, password)

        # set prev msg count
        db_msg_list = self._user.get_message()
        self._prev_msg_count = len(db_msg_list)

        login_successful = False
        if self._user != None:
            login_successful = True

        if login_successful:
            self.openHomePage()
            # pass user to checkMsg and show checkMsg window, then close login window
            self._ui_homePage.label_Username.setText(self._user.get_username())
            # update photo
            self._ui_homePage.label_Photo.setStyleSheet(
                "image: url(" + self._user.get_photo() + ");"
            )
            self.closeLogin()
        else:
            self._ui_login.show_error("User name or password is incorrect.")
            self._ui_login.reset_input()

    def signUp(self):
        (
            user_name,
            password,
            password_check,
            wallet_key,
            email,
            phone,
            size_1024_selected,
            size_2048_selected,
            size_3072_selected,
        ) = self.getSignUpRequest()

        if (
            user_name == ""
            or user_name == None
            or password == ""
            or password == None
            or wallet_key == ""
            or wallet_key == None
            or email == ""
            or email == None
            or phone == ""
            or phone == None
        ):
            self._ui_signUp.show_error("Please check your input.")
        elif (
            size_1024_selected == False
            and size_2048_selected == False
            and size_3072_selected == False
        ):
            self._ui_signUp.show_error("Please check your input.")
        elif password != password_check:
            self._ui_signUp.show_error(
                "Please make sure that the two passwords are the same."
            )
        else:
            # sign up db
            name_registered = False
            name_registered = self._user_factory.is_exist_username(user_name)

            if name_registered:
                self._ui_signUp.show_error(
                    "The user name has been registered.")
            else:
                if size_1024_selected:
                    key_length = 1024
                elif size_2048_selected:
                    key_length = 2048
                else:
                    key_length = 3072

                # db sign up
                user = self._user_factory.create_user(
                    user_name, password, wallet_key, email, phone, key_length
                )

                # blockchain deployment
                deploy_certification(wallet_key)

                # blockchain create certificate for the user
                create_certificate(
                    wallet_key,
                    user_name,
                    email,
                    phone,
                    key_length,
                    user.get_keypairs().get_public_key(),
                )

                # update records in mongoDB(y)
                Record().update_records()

                # set user none
                self._user = None
                self._user_factory.clean_file_content(
                    user.get_keypairs().get_private_key()
                )

                self._ui_signUp.show_info("Sign up successful!")

                self.openLogin()
                self.closeSignUp()

    def updatePhoto(self):
        photo_path = self.getUpdatePhotoRequest()
        # store photo in db
        self._user_factory.update_photo(self._user.get_username(), photo_path)
        # fetch updated user info from db
        self._user = self._user_factory.check_user_by_username(
            self._user.get_username()
        )

        # update photo
        self._ui_homePage.label_Photo.setStyleSheet(
            "image: url(" + self._user.get_photo() + ");"
        )

    def refreshSendMsg(self):
        self._ui_sendMsg
        # update user
        username = self._user.get_username()
        self._user = self._user_factory.check_user_by_username(username)

        # set user name
        self._ui_sendMsg.label_Sender_Username.setText(
            self._user.get_username())

        # private key path from db
        self._ui_sendMsg.label_Private_Key_Location.setText(
            self._user.get_private_key_location()
        )

        user_list = self._user_factory.get_all_username()

        # remove the sender from the receiver list
        user_list.remove(self._user.get_username())

        # add all receivers to combobox
        self._ui_sendMsg.comboBox_Receiver.addItems(user_list)

        # set default public key
        current_receiver_selected = self._ui_sendMsg.comboBox_Receiver.currentText()

        # set public key label to show key length
        # get key len by receiver username
        self._ui_sendMsg.label_RPK.setText(
            "Receiver's publice key("
            + str(self._user_factory.get_key_len(current_receiver_selected))
            + ")"
        )

        # use receiver name get public key
        receiver_public_key = self._user_factory.get_public_key(
            current_receiver_selected
        )
        # bytes to str
        str_receiver_public_key = receiver_public_key.decode("UTF-8")
        self._ui_sendMsg.textEdit_Receiver_Public_Key.setPlainText(
            str_receiver_public_key
        )

        self._ui_sendMsg.comboBox_Receiver.currentTextChanged.connect(
            lambda: {self.send_msg_comboBox_onchange()}
        )

    def send_msg_comboBox_onchange(self):
        current_receiver_selected = self._ui_sendMsg.comboBox_Receiver.currentText()

        # set public key label to show key length
        # get key len by receiver username
        self._ui_sendMsg.label_RPK.setText(
            "Receiver's publice key("
            + str(self._user_factory.get_key_len(current_receiver_selected))
            + ")"
        )

        # use receiver name get public key
        receiver_public_key = self._user_factory.get_public_key(
            current_receiver_selected
        )
        # bytes to str
        str_receiver_public_key = receiver_public_key.decode("UTF-8")
        self._ui_sendMsg.textEdit_Receiver_Public_Key.setPlainText(
            str_receiver_public_key
        )

    def sendMessage(self):
        (
            receiver,
            str_receiver_public_key,
            message,
            private_key_path,
            to_encrypt,
            to_sign,
            to_encrypt_sign,
        ) = self.getSendMsgRequest()

        # str to bytes
        receiver_public_key = str_receiver_public_key.encode("utf-8")

        # message cannot be empty, and the option must be made
        if (
            message == ""
            or message == None
            or (to_encrypt == False and to_sign == False and to_encrypt_sign == False)
        ):
            self._ui_sendMsg.show_error("Please check your input.")
        else:
            message_to_send = ""
            signature_to_send = ""
            delivery_type = ""
            # check option: encrypt, sign or encrypt_sign
            if to_encrypt:
                delivery_type = "ENCRYPTED"
                encrypted_message = encrypt_message(
                    message, receiver_public_key)
                ### db ###########
                message_to_send = encrypted_message

                self._ui_sendMsg.show_info("Message sent!")
            elif to_sign:
                delivery_type = "SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    self._ui_sendMsg.show_error("Private key file not found.")
                else:
                    signature = sign_message(message, private_key_path)
                    ### db ###########
                    message_to_send = message
                    signature_to_send = signature

                    self._ui_sendMsg.show_info("Message sent!")
            else:
                delivery_type = "ENCRYPTED_AND_SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    self._ui_sendMsg.show_error("Private key file not found.")
                else:
                    encrypted_message = encrypt_message(
                        message, receiver_public_key)
                    signature = sign_encrypted_message(
                        encrypted_message, private_key_path
                    )
                    ### db ###########
                    message_to_send = encrypted_message
                    signature_to_send = signature

                    self._ui_sendMsg.show_info("Message sent!")

            msg = Message(
                self._user.get_username(),
                receiver,
                "text",
                message_to_send,
                delivery_type,
            )

            msg.set_signature(signature_to_send)

            # save the send to db
            self._user_factory.insert_message(msg)
            # save private key path to db
            self._user_factory.update_private_key_location(
                private_key_path, self._user.get_username
            )

            self.closeSendMsg()

    def refreshSendFile(self):
        # update user
        username = self._user.get_username()
        self._user = self._user_factory.check_user_by_username(username)

        # set user name
        self._ui_sendFile.label_Sender_Username.setText(
            self._user.get_username())

        # private key path from db
        self._ui_sendFile.label_Private_Key_Location.setText(
            self._user.get_private_key_location()
        )

        user_list = self._user_factory.get_all_username()

        # remove the sender from the receiver list
        user_list.remove(self._user.get_username())

        # add all receivers to combobox
        self._ui_sendFile.comboBox_Receiver.addItems(user_list)

        # set default public key
        current_receiver_selected = self._ui_sendFile.comboBox_Receiver.currentText()

        # set public key label to show key length
        # get key len by receiver username
        self._ui_sendFile.label_RPK.setText(
            "Receiver's publice key("
            + str(self._user_factory.get_key_len(current_receiver_selected))
            + ")"
        )

        # use receiver name get public key
        receiver_public_key = self._user_factory.get_public_key(
            current_receiver_selected
        )

        # bytes to str
        str_receiver_public_key = receiver_public_key.decode("UTF-8")
        self._ui_sendFile.textEdit_Receiver_Public_Key.setPlainText(
            str_receiver_public_key
        )

        self._ui_sendFile.comboBox_Receiver.currentTextChanged.connect(
            lambda: {self.send_file_comboBox_onchange()}
        )

    # def openSendFile(self):
    #     self.refreshSendFile()

    def send_file_comboBox_onchange(self):
        current_receiver_selected = self._ui_sendFile.comboBox_Receiver.currentText()

        # use receiver name get public key
        receiver_public_key = self._user_factory.get_public_key(
            current_receiver_selected
        )
        # bytes to str
        str_receiver_public_key = receiver_public_key.decode("UTF-8")
        self._ui_sendFile.textEdit_Receiver_Public_Key.setPlainText(
            str_receiver_public_key
        )

        # set public key label to show key length
        # get key len by receiver username
        self._ui_sendFile.label_RPK.setText(
            "Receiver's publice key("
            + str(self._user_factory.get_key_len(current_receiver_selected))
            + ")"
        )

    def sendFile(self):
        (
            receiver,
            str_receiver_public_key,
            file_path,
            private_key_path,
            to_encrypt,
            to_sign,
            to_encrypt_sign,
        ) = self.getSendFileRequest()

        # str to bytes
        receiver_public_key = str_receiver_public_key.encode("utf-8")

        # message cannot be empty, and the option must be made
        if (
            file_path == ""
            or file_path == None
            or os.path.exists(file_path) == False
            or (to_encrypt == False and to_sign == False and to_encrypt_sign == False)
        ):
            self._ui_sendFile.show_error("Please check your input.")
        else:
            file_to_send = ""
            signature_to_send = ""
            delivery_type = ""
            # check option: encrypt, sign or encrypt_sign
            if to_encrypt:
                delivery_type = "ENCRYPTED"
                encrypted_file = encrypt_file(file_path, receiver_public_key)
                ### db ###########
                # with open("file/encrypted_file.bin", "wb") as fp:
                #     fp.write(encrypted_file)

                # path = file_path.split("/")[-1]
                # with open("file/file_to_save.bin", "wb") as fp:
                #     fp.write(encrypted_file)

                # set message.message
                file_byte = encrypted_file

                file_to_send = "file/" + file_path.split("/")[-1]

                self._ui_sendFile.show_info("File sent!")
            elif to_sign:
                delivery_type = "SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    self._ui_sendFile.show_error("Private key file not found.")
                else:
                    signature = sign_file(private_key_path, file_path)
                    ### db ###########

                    file_byte = self._user_factory.file_to_byte(file_path)

                    file_to_send = file_path
                    signature_to_send = signature

                    self._ui_sendFile.show_info("File sent!")
            else:
                delivery_type = "ENCRYPTED_AND_SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    self._ui_sendFile.show_error("Private key file not found.")
                else:
                    encrypted_file = encrypt_file(
                        file_path, receiver_public_key)
                    signature = sign_encrypted_file(
                        private_key_path, encrypted_file)
                    ### db ###########
                    # with open("file/encrypted_and_signed_file.bin", "wb") as fp:
                    #     fp.write(encrypted_file)

                    # path = file_path.split("/")[-1]
                    # with open("file/file_to_save.bin", "wb") as fp:
                    #     fp.write(encrypted_file)

                    file_byte = encrypted_file

                    file_to_send = "file/" + file_path.split("/")[-1]

                    signature_to_send = signature

                    self._ui_sendFile.show_info("File sent!")

            msg = Message(
                self._user.get_username(),
                receiver,
                "file",
                file_to_send,
                delivery_type,
            )

            msg.set_signature(signature_to_send)

            # save the send to db
            self._user_factory.insert_message_with_file(msg, file_byte)
            # save private key path to db
            self._user_factory.update_private_key_location(
                private_key_path, self._user.get_username
            )
            # delete file cache
            self._user_factory.delete_file(file_to_send)

            self.closeSendFile()

    def onTableSelectionChanged(self):
        selected = self._ui_checkMsg.tableWidget_Message.selectionModel().selection()
        # reset message board when table selection changed
        self._ui_checkMsg.text_Message.setPlainText("")
        selected_list = selected.indexes()
        sender = self._ui_checkMsg.tableWidget_Message.item(
            selected_list[0].row(), selected_list[0].column()
        ).text()
        timestamp = self._ui_checkMsg.tableWidget_Message.item(
            selected_list[2].row(), selected_list[2].column()
        ).text()

        self._m_selected = None

        for m in self._user.get_message():
            if (
                m["sender"] == sender
                and m["timestamp"].strftime("%m/%d/%Y, %H:%M:%S") == timestamp
            ):
                self._m_selected = m
                break

        # enable and disable buttons according to delivery type
        if self._m_selected["delivery_type"] == "ENCRYPTED":
            self._ui_checkMsg.pushButton_Decrypt.setEnabled(True)
            self._ui_checkMsg.pushButton_Validate.setEnabled(False)
        elif self._m_selected["delivery_type"] == "SIGNED":
            self._ui_checkMsg.pushButton_Decrypt.setEnabled(False)
            self._ui_checkMsg.pushButton_Validate.setEnabled(True)
        elif self._m_selected["delivery_type"] == "ENCRYPTED_AND_SIGNED":
            self._ui_checkMsg.pushButton_Decrypt.setEnabled(True)
            self._ui_checkMsg.pushButton_Validate.setEnabled(True)

        # change label show and show the filename if message type is file
        if self._m_selected["message_type"] == "file":
            f_info = self._user_factory.get_file_by_id(
                self._m_selected["message"])
            self._ui_checkMsg.text_Message.setPlainText(f_info["file_name"])
            self._ui_checkMsg.label.setText("Filename")
        # show msg if type is msg
        else:
            self._ui_checkMsg.label.setText("Message")

    def refreshCheckMsg(self):
        # set remembered private key file path
        self._ui_checkMsg.label_Private_Key_Location.setText(
            self._user.get_private_key_location()
        )

        self._ui_checkMsg.label.setText("Message")
        # self._ui_checkMsg.pushButton_Decrypt.clicked.connect(
        #     lambda: {self.decrypt()})
        # self._ui_checkMsg.pushButton_Validate.clicked.connect(
        #     lambda: {self.verify()})
        # self._ui_checkMsg.pushButton_Download_The_File.clicked.connect(
        #     lambda: {self.downloadFile()}
        # )
        # init disable buttons
        self._ui_checkMsg.pushButton_Decrypt.setEnabled(False)
        self._ui_checkMsg.pushButton_Validate.setEnabled(False)
        self._ui_checkMsg.pushButton_Download_The_File.setEnabled(False)

        # update user
        username = self._user.get_username()
        self._user = self._user_factory.check_user_by_username(username)

        # received msg list
        msg_list = self._user.get_message()
        msg_count = len(msg_list)
        self._ui_checkMsg.tableWidget_Message.setColumnCount(4)
        self._ui_checkMsg.tableWidget_Message.setRowCount(msg_count)

        self._ui_checkMsg.tableWidget_Message.selectionModel().selectionChanged.connect(
            lambda: {self.onTableSelectionChanged()}
        )

        # for loop in table
        for i in range(0, msg_count):
            # every row
            item = QtWidgets.QTableWidgetItem()

            # row header index
            self._ui_checkMsg.tableWidget_Message.setVerticalHeaderItem(
                i, item)
            row_header_item = self._ui_checkMsg.tableWidget_Message.verticalHeaderItem(
                i
            )
            row_header_item.setText(str(i + 1))

            # 4 items in a row
            self._ui_checkMsg.tableWidget_Message.setItem(
                i, 0, QTableWidgetItem(msg_list[i]["sender"])
            )
            self._ui_checkMsg.tableWidget_Message.setItem(
                i, 1, QTableWidgetItem(msg_list[i]["message_type"])
            )
            self._ui_checkMsg.tableWidget_Message.setItem(
                i,
                2,
                QTableWidgetItem(
                    msg_list[i]["timestamp"].strftime("%m/%d/%Y, %H:%M:%S")
                ),
            )
            self._ui_checkMsg.tableWidget_Message.setItem(
                i, 3, QTableWidgetItem(msg_list[i]["delivery_type"])
            )

    def decrypt(self):
        # save private key path to db
        self._user_factory.update_private_key_location(
            self._ui_checkMsg.label_Private_Key_Location.text(), self._user.get_username
        )

        # if msg type is text
        if self._m_selected["message_type"] == "text":
            # decrypt msg
            decrypted_message = decrypt_message(
                self._m_selected["message"],
                self._ui_checkMsg.label_Private_Key_Location.text(),
            )
            # show decrypted msg
            self._ui_checkMsg.text_Message.setPlainText(decrypted_message)
        # if msg type is file
        else:
            f_info = self._user_factory.get_file_by_id(
                self._m_selected["message"])
            filename = f_info["file_name"]

            encrypted_file = f_info["file"]
            # with open("file/" + filename, "rb") as fp:
            #     encrypted_file = fp.read()

            # decrypt file
            decrypt_file(
                encrypted_file,
                "file_to_save.bin",
                self._ui_checkMsg.label_Private_Key_Location.text(),
                # get current user public key len
                self._user.get_keypairs().get_length(),
            )
            self._ui_checkMsg.pushButton_Download_The_File.setEnabled(True)

    def downloadFile(self):
        response = QFileDialog.getExistingDirectory(
            None, caption="Select a folder")

        f_info = self._user_factory.get_file_by_id(self._m_selected["message"])
        filename = f_info["file_name"]

        with open("file/file_to_save.bin", "rb") as fp:
            file_save = fp.read()

        with open(response + "/" + filename, "wb") as fb:
            fb.write(file_save)

        self._ui_checkMsg.show_info("File has been downloaded.")

    def verify(self):
        # save private key path to db
        self._user_factory.update_private_key_location(
            self._ui_checkMsg.label_Private_Key_Location.text(), self._user.get_username
        )

        if self._m_selected["delivery_type"] == "ENCRYPTED_AND_SIGNED":
            # if msg type is text
            if self._m_selected["message_type"] == "text":
                # print(
                #     "pv", self._user_factory.get_public_key(self._m_selected["sender"])
                # )

                # whether verify msg successfully
                signed_message_succ = verify_encryptedMessage(
                    self._m_selected["message"],
                    self._m_selected["signature"],
                    self._user_factory.get_public_key(
                        self._m_selected["sender"]),
                )

                # # show msg
                # ui_checkMsg.text_Message.setPlashowinText(self._m_selected["message"])

                if signed_message_succ:
                    self._ui_checkMsg.show_info("Verify Successful")
                else:
                    self._ui_checkMsg.show_info("Verify Failed")

            # if msg type is file
            else:
                f_info = self._user_factory.get_file_by_id(
                    self._m_selected["message"])
                filename = f_info["file_name"]
                # with open("file/file_to_save.bin", "rb") as fp:
                #     encrypted_file = fp.read()
                encrypted_file = f_info["file"]

                # verify file
                signed_file_succ = verify_encrypted_file(
                    self._m_selected["signature"],
                    encrypted_file,
                    self._user_factory.get_public_key(
                        self._m_selected["sender"]),
                    self._user_factory.get_key_len(self._m_selected["sender"]),
                )

                if signed_file_succ:
                    self._ui_checkMsg.show_info("Verify Successful")
                    self._ui_checkMsg.pushButton_Download_The_File.setEnabled(
                        True)
                else:
                    self._ui_checkMsg.show_info("Verify Failed")
        else:
            # if msg type is text
            if self._m_selected["message_type"] == "text":
                # whether verify msg successfully
                signed_message_succ = verify_signature(
                    self._m_selected["message"],
                    self._m_selected["signature"],
                    self._user_factory.get_public_key(
                        self._m_selected["sender"]),
                )
                # show msg
                self._ui_checkMsg.text_Message.setPlainText(
                    self._m_selected["message"])

                if signed_message_succ:
                    self._ui_checkMsg.show_info("Verify Successful")
                else:
                    self._ui_checkMsg.show_info("Verify Failed")

            # if msg type is file
            else:
                f_info = self._user_factory.get_file_by_id(
                    self._m_selected["message"])

                # decode the plain_file
                plain_file = base64.b64decode(f_info["file"])

                # verify file
                signed_file_succ = verify_file(
                    self._m_selected["signature"],
                    plain_file,
                    self._user_factory.get_public_key(
                        self._m_selected["sender"]),
                    # get sender's key len
                    self._user_factory.get_key_len(self._m_selected["sender"]),
                )

                if signed_file_succ:
                    self._ui_checkMsg.show_info("Verify Successful")
                    # write file into file_to_save.bin
                    with open("file/file_to_save.bin", "wb") as fp:
                        fp.write(plain_file)
                    self._ui_checkMsg.pushButton_Download_The_File.setEnabled(
                        True)
                else:
                    self._ui_checkMsg.show_info("Verify Failed")
