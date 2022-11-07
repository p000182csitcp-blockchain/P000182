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


class Init:
    def __init__(self) -> None:
        self._user = None
        self._user_factory = UserFactory()
        self._m_selected = None

    def start_ui(self):
        app = QApplication([])
        # Log in page widget
        window_login = QMainWindow()
        ui_login = Ui_Login()
        ui_login.setupUi(window_login)
        window_login.show()

        # Sign up page widget
        window_signup = QMainWindow()
        ui_signup = Ui_Sign_Up()
        ui_signup.setupUi(window_signup)

        # Home page widget
        window_homepage = QMainWindow()
        ui_homepage = Ui_Homepage()
        ui_homepage.setupUi(window_homepage)

        # SendMsg page widget
        window_sendMsg = QMainWindow()
        ui_sendMsg = Ui_Send_Message()
        ui_sendMsg.setupUi(window_sendMsg)

        # SendFile page widget
        window_sendFile = QMainWindow()
        ui_sendFile = Ui_Send_File()
        ui_sendFile.setupUi(window_sendFile)

        # Check msg page widget
        window_checkMsg = QMainWindow()
        ui_checkMsg = Ui_Check_Message()
        ui_checkMsg.setupUi(window_checkMsg)

        # Login to Sign up button event
        ui_login.pushButton_register.clicked.connect(
            lambda: {window_signup.show(), window_login.close()}
        )

        # Login button event
        ui_login.pushButton_Login.clicked.connect(
            lambda: {
                self.login(
                    ui_login.loginRequest(),
                    ui_homepage,
                    window_homepage,
                    ui_login,
                    window_login,
                )
            }
        )

        # Sign up to Login button event
        ui_signup.pushButton_Login.clicked.connect(
            lambda: {window_login.show(), window_signup.close()}
        )

        # Signup button event
        ui_signup.pushButton_Sign_Up.clicked.connect(
            lambda: {
                self.signUp(
                    ui_signup.signUpRequest(),
                    window_login,
                    ui_signup,
                    window_signup,
                )
            }
        )

        # Home page log out
        ui_homepage.pushButton_Log_Out.clicked.connect(
            lambda: {window_login.show(), window_homepage.close()}
        )

        # Home page update photo
        ui_homepage.pushButton_Update_photo.clicked.connect(
            lambda: {self.updatePhoto(ui_homepage.updatePhotoRequest(), ui_homepage)}
        )

        # Main page go to send message page
        ui_homepage.pushButton_Send_Message.clicked.connect(
            lambda: {self.openSendMsg(ui_sendMsg), window_sendMsg.show()}
        )

        # Main page go to send file page
        ui_homepage.pushButton_Send_File.clicked.connect(
            lambda: {self.openSendFile(ui_sendFile), window_sendFile.show()}
        )

        # Main page go to message list page
        ui_homepage.pushButton_Check_Message.clicked.connect(
            lambda: {self.openCheckMsg(ui_checkMsg), window_checkMsg.show()}
        )

        # send message page send button event
        ui_sendMsg.pushButton_Send.clicked.connect(
            lambda: {
                self.sendMessage(
                    ui_sendMsg.sendingRequest(), window_sendMsg, ui_sendMsg
                )
            }
        )

        # send file page send button event
        ui_sendFile.pushButton_Send.clicked.connect(
            lambda: {
                self.sendFile(
                    ui_sendFile.sendingRequest(), window_sendFile, ui_sendFile
                )
            }
        )

        sys.exit(app.exec_())

    def login(self, login_info, ui_homepage, window_homepage, ui_login, window_login):
        user_name, password = login_info
        # login db
        self._user = self._user_factory.check_user(user_name, password)
        login_successful = False
        if self._user != None:
            login_successful = True

        if login_successful:
            # pass user to checkMsg and show checkMsg window, then close login window
            ui_homepage.label_Username.setText(self._user.get_username())
            # update photo
            ui_homepage.label_Photo.setStyleSheet(
                "image: url(" + self._user.get_photo() + ");"
            )
            window_homepage.show()
            window_login.close()
        else:
            ui_login.show_error("User name or password is incorrect.")
            ui_login.reset_input()

    def signUp(self, sign_up_info, window_login, ui_signup, window_signup):
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
        ) = sign_up_info

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
            ui_signup.show_error("Please check your input.")
        elif (
            size_1024_selected == False
            and size_2048_selected == False
            and size_3072_selected == False
        ):
            ui_signup.show_error("Please check your input.")
        elif password != password_check:
            ui_signup.show_error(
                "Please make sure that the two passwords are the same."
            )
        else:
            # sign up db
            name_registered = False
            name_registered = self._user_factory.is_exist_username(user_name)

            if name_registered:
                ui_signup.show_error("The user name has been registered.")
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

                ui_signup.show_info("Sign up successful!")

                window_login.show()
                window_signup.close()

    def updatePhoto(self, photo_path, ui_homepage):
        # store photo in db
        self._user_factory.update_photo(self._user.get_username(), photo_path)
        # fetch updated user info from db
        self._user = self._user_factory.check_user_by_username(
            self._user.get_username()
        )
        # for test
        # self._user = self._user_factory.check_user(self._user.get_username(), "123")

        # update photo
        ui_homepage.label_Photo.setStyleSheet(
            "image: url(" + self._user.get_photo() + ");"
        )

    def openSendMsg(self, ui_sendMsg):
        # update user
        username = self._user.get_username()
        self._user = self._user_factory.check_user_by_username(username)

        # set user name
        ui_sendMsg.label_Sender_Username.setText(self._user.get_username())

        # private key path from db
        ui_sendMsg.label_Private_Key_Location.setText(
            self._user.get_private_key_location()
        )

        user_list = self._user_factory.get_all_username()

        # remove the sender from the receiver list
        user_list.remove(self._user.get_username())

        # add all receivers to combobox
        ui_sendMsg.comboBox_Receiver.addItems(user_list)

        # set default public key
        current_receiver_selected = ui_sendMsg.comboBox_Receiver.currentText()

        # set public key label to show key length
        # get key len by receiver username
        ui_sendMsg.label_RPK.setText(
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
        ui_sendMsg.textEdit_Receiver_Public_Key.setPlainText(str_receiver_public_key)

        ui_sendMsg.comboBox_Receiver.currentTextChanged.connect(
            lambda: {self.send_msg_comboBox_onchange(ui_sendMsg)}
        )

    def send_msg_comboBox_onchange(self, ui_sendMsg):
        current_receiver_selected = ui_sendMsg.comboBox_Receiver.currentText()

        # set public key label to show key length
        # get key len by receiver username
        ui_sendMsg.label_RPK.setText(
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
        ui_sendMsg.textEdit_Receiver_Public_Key.setPlainText(str_receiver_public_key)

    def sendMessage(self, send_info, window_sendMsg, ui_sendMsg):
        (
            receiver,
            str_receiver_public_key,
            message,
            private_key_path,
            to_encrypt,
            to_sign,
            to_encrypt_sign,
        ) = send_info

        # str to bytes
        receiver_public_key = str_receiver_public_key.encode("utf-8")

        # message cannot be empty, and the option must be made
        if (
            message == ""
            or message == None
            or (to_encrypt == False and to_sign == False and to_encrypt_sign == False)
        ):
            ui_sendMsg.show_error("Please check your input.")
        else:
            message_to_send = ""
            signature_to_send = ""
            delivery_type = ""
            # check option: encrypt, sign or encrypt_sign
            if to_encrypt:
                delivery_type = "ENCRYPTED"
                encrypted_message = encrypt_message(message, receiver_public_key)
                ### db ###########
                message_to_send = encrypted_message

                ui_sendMsg.show_info("Message sent!")
                window_sendMsg.close()
            elif to_sign:
                delivery_type = "SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    ui_sendMsg.show_error("Private key file not found.")
                else:
                    signature = sign_message(message, private_key_path)
                    ### db ###########
                    message_to_send = message
                    signature_to_send = signature

                    ui_sendMsg.show_info("Message sent!")
                    window_sendMsg.close()
            else:
                delivery_type = "ENCRYPTED_AND_SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    ui_sendMsg.show_error("Private key file not found.")
                else:
                    encrypted_message = encrypt_message(message, receiver_public_key)
                    signature = sign_encrypted_message(
                        encrypted_message, private_key_path
                    )
                    ### db ###########
                    message_to_send = encrypted_message
                    signature_to_send = signature

                    ui_sendMsg.show_info("Message sent!")
                    window_sendMsg.close()

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

    def openSendFile(self, ui_sendFile):
        # update user
        username = self._user.get_username()
        self._user = self._user_factory.check_user_by_username(username)

        # set user name
        ui_sendFile.label_Sender_Username.setText(self._user.get_username())

        # private key path from db
        ui_sendFile.label_Private_Key_Location.setText(
            self._user.get_private_key_location()
        )

        user_list = self._user_factory.get_all_username()

        # remove the sender from the receiver list
        user_list.remove(self._user.get_username())

        # add all receivers to combobox
        ui_sendFile.comboBox_Receiver.addItems(user_list)

        # set default public key
        current_receiver_selected = ui_sendFile.comboBox_Receiver.currentText()

        # set public key label to show key length
        # get key len by receiver username
        ui_sendFile.label_RPK.setText(
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
        ui_sendFile.textEdit_Receiver_Public_Key.setPlainText(str_receiver_public_key)

        ui_sendFile.comboBox_Receiver.currentTextChanged.connect(
            lambda: {self.send_file_comboBox_onchange(ui_sendFile)}
        )

    def send_file_comboBox_onchange(self, ui_sendFile):
        current_receiver_selected = ui_sendFile.comboBox_Receiver.currentText()

        # use receiver name get public key
        receiver_public_key = self._user_factory.get_public_key(
            current_receiver_selected
        )
        # bytes to str
        str_receiver_public_key = receiver_public_key.decode("UTF-8")
        ui_sendFile.textEdit_Receiver_Public_Key.setPlainText(str_receiver_public_key)

        # set public key label to show key length
        # get key len by receiver username
        ui_sendFile.label_RPK.setText(
            "Receiver's publice key("
            + str(self._user_factory.get_key_len(current_receiver_selected))
            + ")"
        )

    def sendFile(self, send_info, window_sendFile, ui_sendFile):
        (
            receiver,
            str_receiver_public_key,
            file_path,
            private_key_path,
            to_encrypt,
            to_sign,
            to_encrypt_sign,
        ) = send_info

        # str to bytes
        receiver_public_key = str_receiver_public_key.encode("utf-8")

        # message cannot be empty, and the option must be made
        if (
            file_path == ""
            or file_path == None
            or os.path.exists(file_path) == False
            or (to_encrypt == False and to_sign == False and to_encrypt_sign == False)
        ):
            ui_sendFile.show_error("Please check your input.")
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

                ui_sendFile.show_info("File sent!")
                window_sendFile.close()
            elif to_sign:
                delivery_type = "SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    ui_sendFile.show_error("Private key file not found.")
                else:
                    signature = sign_file(private_key_path, file_path)
                    ### db ###########

                    file_byte = self._user_factory.file_to_byte(file_path)

                    file_to_send = file_path
                    signature_to_send = signature

                    ui_sendFile.show_info("File sent!")
                    window_sendFile.close()
            else:
                delivery_type = "ENCRYPTED_AND_SIGNED"
                # check if private key file exit
                isPrivateKeyFileExist = os.path.exists(private_key_path)
                if isPrivateKeyFileExist == False:
                    ui_sendFile.show_error("Private key file not found.")
                else:
                    encrypted_file = encrypt_file(file_path, receiver_public_key)
                    signature = sign_encrypted_file(private_key_path, encrypted_file)
                    ### db ###########
                    # with open("file/encrypted_and_signed_file.bin", "wb") as fp:
                    #     fp.write(encrypted_file)

                    # path = file_path.split("/")[-1]
                    # with open("file/file_to_save.bin", "wb") as fp:
                    #     fp.write(encrypted_file)

                    file_byte = encrypted_file

                    file_to_send = "file/" + file_path.split("/")[-1]

                    signature_to_send = signature

                    ui_sendFile.show_info("File sent!")
                    window_sendFile.close()

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

    def onTableSelectionChanged(self, selected, ui_checkMsg):
        # rest message board when table selection changed
        ui_checkMsg.text_Message.setPlainText("")
        selected_list = selected.indexes()
        # sender = selected_list[0].text()
        # timestamp = selected_list[2]
        sender = ui_checkMsg.tableWidget_Message.item(
            selected_list[0].row(), selected_list[0].column()
        ).text()
        timestamp = ui_checkMsg.tableWidget_Message.item(
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
            ui_checkMsg.pushButton_Decrypt.setEnabled(True)
            ui_checkMsg.pushButton_Validate.setEnabled(False)
        elif self._m_selected["delivery_type"] == "SIGNED":
            ui_checkMsg.pushButton_Decrypt.setEnabled(False)
            ui_checkMsg.pushButton_Validate.setEnabled(True)
        elif self._m_selected["delivery_type"] == "ENCRYPTED_AND_SIGNED":
            ui_checkMsg.pushButton_Decrypt.setEnabled(True)
            ui_checkMsg.pushButton_Validate.setEnabled(True)

        # change label show and show the filename if message type is file
        if self._m_selected["message_type"] == "file":
            f_info = self._user_factory.get_file_by_id(self._m_selected["message"])
            ui_checkMsg.text_Message.setPlainText(f_info["file_name"])
            ui_checkMsg.label.setText("Filename")

    def openCheckMsg(self, ui_checkMsg):
        # set remembered private key file path
        ui_checkMsg.label_Private_Key_Location.setText(
            self._user.get_private_key_location()
        )

        ui_checkMsg.label.setText("Message")
        ui_checkMsg.pushButton_Decrypt.clicked.connect(
            lambda: {self.decrypt(ui_checkMsg)}
        )
        ui_checkMsg.pushButton_Validate.clicked.connect(
            lambda: {self.verify(ui_checkMsg)}
        )
        ui_checkMsg.pushButton_Download_The_File.clicked.connect(
            lambda: {self.downloadFile(ui_checkMsg)}
        )
        # init disable buttons
        ui_checkMsg.pushButton_Decrypt.setEnabled(False)
        ui_checkMsg.pushButton_Validate.setEnabled(False)
        ui_checkMsg.pushButton_Download_The_File.setEnabled(False)

        # update user
        username = self._user.get_username()
        self._user = self._user_factory.check_user_by_username(username)

        # received msg list
        msg_list = self._user.get_message()
        msg_count = len(msg_list)
        ui_checkMsg.tableWidget_Message.setColumnCount(4)
        ui_checkMsg.tableWidget_Message.setRowCount(msg_count)

        ui_checkMsg.tableWidget_Message.selectionModel().selectionChanged.connect(
            lambda: {
                self.onTableSelectionChanged(
                    ui_checkMsg.tableWidget_Message.selectionModel().selection(),
                    ui_checkMsg,
                )
            }
        )

        # for loop
        for i in range(0, msg_count):
            # every row
            item = QtWidgets.QTableWidgetItem()

            # row header index
            ui_checkMsg.tableWidget_Message.setVerticalHeaderItem(i, item)
            row_header_item = ui_checkMsg.tableWidget_Message.verticalHeaderItem(i)
            row_header_item.setText(str(i + 1))

            # 4 items in a row
            ui_checkMsg.tableWidget_Message.setItem(
                i, 0, QTableWidgetItem(msg_list[i]["sender"])
            )
            ui_checkMsg.tableWidget_Message.setItem(
                i, 1, QTableWidgetItem(msg_list[i]["message_type"])
            )
            ui_checkMsg.tableWidget_Message.setItem(
                i,
                2,
                QTableWidgetItem(
                    msg_list[i]["timestamp"].strftime("%m/%d/%Y, %H:%M:%S")
                ),
            )
            ui_checkMsg.tableWidget_Message.setItem(
                i, 3, QTableWidgetItem(msg_list[i]["delivery_type"])
            )

    def decrypt(self, ui_checkMsg):
        # save private key path to db
        self._user_factory.update_private_key_location(
            ui_checkMsg.label_Private_Key_Location.text(), self._user.get_username
        )

        # if msg type is text
        if self._m_selected["message_type"] == "text":
            # decrypt msg
            decrypted_message = decrypt_message(
                self._m_selected["message"],
                ui_checkMsg.label_Private_Key_Location.text(),
            )
            # show decrypted msg
            ui_checkMsg.text_Message.setPlainText(decrypted_message)
        # if msg type is file
        else:
            f_info = self._user_factory.get_file_by_id(self._m_selected["message"])
            filename = f_info["file_name"]

            encrypted_file = f_info["file"]
            # with open("file/" + filename, "rb") as fp:
            #     encrypted_file = fp.read()

            # decrypt file
            decrypt_file(
                encrypted_file,
                "file_to_save.bin",
                ui_checkMsg.label_Private_Key_Location.text(),
                # get current user public key len
                self._user.get_keypairs().get_length(),
            )
            ui_checkMsg.pushButton_Download_The_File.setEnabled(True)

    def downloadFile(self, ui_checkMsg):
        response = QFileDialog.getExistingDirectory(None, caption="Select a folder")

        f_info = self._user_factory.get_file_by_id(self._m_selected["message"])
        filename = f_info["file_name"]

        with open("file/file_to_save.bin", "rb") as fp:
            file_save = fp.read()

        with open(response + "/" + filename, "wb") as fb:
            fb.write(file_save)

        ui_checkMsg.show_info("File has been downloaded.")

    def verify(self, ui_checkMsg):
        # save private key path to db
        self._user_factory.update_private_key_location(
            ui_checkMsg.label_Private_Key_Location.text(), self._user.get_username
        )

        if self._m_selected["delivery_type"] == "ENCRYPTED_AND_SIGNED":
            # if msg type is text
            if self._m_selected["message_type"] == "text":
                print(
                    "pv", self._user_factory.get_public_key(self._m_selected["sender"])
                )

                # whether verify msg successfully
                signed_message_succ = verify_encryptedMessage(
                    self._m_selected["message"],
                    self._m_selected["signature"],
                    self._user_factory.get_public_key(self._m_selected["sender"]),
                )

                # # show msg
                # ui_checkMsg.text_Message.setPlashowinText(self._m_selected["message"])

                if signed_message_succ:
                    ui_checkMsg.show_info("Verify Successful")
                else:
                    ui_checkMsg.show_info("Verify Failed")

            # if msg type is file
            else:
                f_info = self._user_factory.get_file_by_id(self._m_selected["message"])
                filename = f_info["file_name"]
                # with open("file/file_to_save.bin", "rb") as fp:
                #     encrypted_file = fp.read()
                encrypted_file = f_info["file"]

                # verify file
                signed_file_succ = verify_encrypted_file(
                    self._m_selected["signature"],
                    encrypted_file,
                    self._user_factory.get_public_key(self._m_selected["sender"]),
                    self._user_factory.get_key_len(self._m_selected["sender"]),
                )

                if signed_file_succ:
                    ui_checkMsg.show_info("Verify Successful")
                    ui_checkMsg.pushButton_Download_The_File.setEnabled(True)
                else:
                    ui_checkMsg.show_info("Verify Failed")
        else:
            # if msg type is text
            if self._m_selected["message_type"] == "text":
                # whether verify msg successfully
                signed_message_succ = verify_signature(
                    self._m_selected["message"],
                    self._m_selected["signature"],
                    self._user_factory.get_public_key(self._m_selected["sender"]),
                )
                # show msg
                ui_checkMsg.text_Message.setPlainText(self._m_selected["message"])

                if signed_message_succ:
                    ui_checkMsg.show_info("Verify Successful")
                else:
                    ui_checkMsg.show_info("Verify Failed")

            # if msg type is file
            else:
                f_info = self._user_factory.get_file_by_id(self._m_selected["message"])

                # decode the plain_file
                plain_file = base64.b64decode(f_info["file"])

                # verify file
                signed_file_succ = verify_file(
                    self._m_selected["signature"],
                    plain_file,
                    self._user_factory.get_public_key(self._m_selected["sender"]),
                    # get sender's key len
                    self._user_factory.get_key_len(self._m_selected["sender"]),
                )

                if signed_file_succ:
                    ui_checkMsg.show_info("Verify Successful")
                    # write file into file_to_save.bin
                    with open("file/file_to_save.bin", "wb") as fp:
                        fp.write(plain_file)
                    ui_checkMsg.pushButton_Download_The_File.setEnabled(True)
                else:
                    ui_checkMsg.show_info("Verify Failed")
