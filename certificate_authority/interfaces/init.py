from PyQt5 import QtCore, QtGui, QtWidgets
# from interfaces.Login import Ui_Login
# from interfaces.Sign_Up import Ui_Sign_Up
# from interfaces.Homepage import Ui_Homepage
# from interfaces.Send_Message import Ui_Send_Message
# from interfaces.Check_Message import Ui_Check_Message
from interfaces.Send_File import Ui_Send_File
from scripts.crypto import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


def start_ui():
    app = QApplication([])
    # # Log in page widget
    # window_login = QMainWindow()
    # ui_login = Ui_Login()
    # ui_login.setupUi(window_login)
    # window_login.show()

    # # Sign up page widget
    # window_signup = QMainWindow()
    # ui_signup = Ui_Sign_Up()
    # ui_signup.setupUi(window_signup)

    # # Home page widget
    # window_homepage = QMainWindow()
    # ui_homepage = Ui_Homepage()
    # ui_homepage.setupUi(window_homepage)

    # # SendMsg page widget
    # window_sendMsg = QMainWindow()
    # ui_sendMsg = Ui_Send_Message()
    # ui_sendMsg.setupUi(window_sendMsg)

    # SendFile page widget
    window_sendFile = QMainWindow()
    ui_sendFile = Ui_Send_File()
    ui_sendFile.setupUi(window_sendFile)

    # # Check msg page widget
    # window_checkMsg = QMainWindow()
    # ui_checkMsg = Ui_Check_Message()
    # ui_checkMsg.setupUi(window_checkMsg)

    # # Login to Sign up button event
    # ui_login.pushButton_register.clicked.connect(
    #     lambda: {window_signup.show(), window_login.close()}
    # )

    # # Login button event
    # ui_login.pushButton_Login.clicked.connect(
    #     lambda: {
    #         login(
    #             ui_login.loginRequest(),
    #             ui_homepage,
    #             window_homepage,
    #             ui_login,
    #             window_login,
    #         )
    #     }
    # )

    # # Sign up to Login button event
    # ui_signup.pushButton_Login.clicked.connect(
    #     lambda: {window_login.show(), window_signup.close()}
    # )

    # # Signup button event
    # ui_signup.pushButton_Sign_Up.clicked.connect(
    #     lambda: {
    #         signUp(
    #             ui_signup.signUpRequest(),
    #             window_login,
    #             ui_signup,
    #             window_signup,
    #         )
    #     }
    # )

    # # Main page go to send message page
    # ui_homepage.pushButton_Send_Message.clicked.connect(lambda: {window_sendMsg.show()})

    # # Main page go to send file page
    # ui_homepage.pushButton_Send_File.clicked.connect(lambda: {window_sendFile.show()})

    # # Main page go to message list page
    # ui_homepage.pushButton_Check_Message.clicked.connect(
    #     lambda: {window_checkMsg.show()}
    # )

    # # send message page send button event
    # ui_sendMsg.pushButton_Send.clicked.connect(
    #     lambda: {sendMessage(ui_sendMsg.sendingRequest(), window_sendMsg, ui_sendMsg)}
    # )

    # send file page send button event
    ui_sendFile.pushButton_Send.clicked.connect(
        lambda: {sendFile(ui_sendFile.sendingRequest(), window_sendFile, ui_sendFile)}
    )

    sys.exit(app.exec_())


def login(login_info, ui_homepage, window_homepage, ui_login, window_login):
    user_name, password = login_info
    # login db
    login_successful = True
    user = None

    if login_successful:
        # pass user to checkMsg and show checkMsg window, then close login window
        ui_homepage.setUser(user)
        window_homepage.show()
        window_login.close()
    else:
        ui_login.show_error("User name or password is incorrect.")
        ui_login.reset_input()


def signUp(sign_up_info, window_login, ui_signup, window_signup):
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

    # sign up db
    name_registered = False
    wallet_key_registered = False

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
        ui_signup.show_error("Please make sure that the two passwords are the same.")
    elif name_registered:
        ui_signup.show_error("The user name has been registered.")
    elif wallet_key_registered:
        ui_signup.show_error("The wallet private key has been registered.")
    else:
        # blockchain deployment

        # db sign up

        window_login.show()
        window_signup.close()


def sendMessage(send_info, window_sendMsg, ui_sendMsg):
    (
        receiver,
        receiver_public_key,
        message,
        private_key_path,
        to_encrypt,
        to_sign,
        to_encrypt_sign,
    ) = send_info

    # message cannot be empty, and the option must be made
    if (
        message == ""
        or message == None
        or (to_encrypt == False and to_sign == False and to_encrypt_sign == False)
    ):
        ui_sendMsg.show_error("Please check your input.")
    else:
        # check option: encrypt, sign or encrypt_sign
        if to_encrypt:
            encrypted_message = encrypt_message(message, receiver_public_key)
            ### db ###########

            ui_sendMsg.show_info("Message sent!")
            window_sendMsg.close()
        elif to_sign:
            # check if private key file exit
            isPrivateKeyFileExist = os.path.exists(private_key_path)
            if isPrivateKeyFileExist == False:
                ui_sendMsg.show_error("Private key file not found.")
            else:
                signature = sign_message(message, private_key_path)
                ### db ###########

                ui_sendMsg.show_info("Message sent!")
                window_sendMsg.close()
        else:
            # check if private key file exit
            isPrivateKeyFileExist = os.path.exists(private_key_path)
            if isPrivateKeyFileExist == False:
                ui_sendMsg.show_error("Private key file not found.")
            else:
                encrypted_message = encrypt_message(message, receiver_public_key)
                signature = sign_encrypted_message(encrypted_message, private_key_path)
                ### db ###########

                ui_sendMsg.show_info("Message sent!")
                window_sendMsg.close()


def sendFile(send_info, window_sendFile, ui_sendFile):
    (
        receiver,
        receiver_public_key,
        file_path,
        private_key_path,
        to_encrypt,
        to_sign,
        to_encrypt_sign,
    ) = send_info

    # message cannot be empty, and the option must be made
    if (
        file_path == ""
        or file_path == None
        or os.path.exists(file_path) == False
        or (to_encrypt == False and to_sign == False and to_encrypt_sign == False)
    ):
        ui_sendFile.show_error("Please check your input.")
    else:
        # check option: encrypt, sign or encrypt_sign
        if to_encrypt:
            encrypted_file = encrypt_file(file_path, receiver_public_key)
            ### db ###########

            ui_sendFile.show_info("File sent!")
            window_sendFile.close()
        elif to_sign:
            # check if private key file exit
            isPrivateKeyFileExist = os.path.exists(private_key_path)
            if isPrivateKeyFileExist == False:
                ui_sendFile.show_error("Private key file not found.")
            else:
                signature = sign_file(private_key_path, file_path)
                ### db ###########

                ui_sendFile.show_info("File sent!")
                window_sendFile.close()
        else:
            # check if private key file exit
            isPrivateKeyFileExist = os.path.exists(private_key_path)
            if isPrivateKeyFileExist == False:
                ui_sendFile.show_error("Private key file not found.")
            else:
                encrypted_file = encrypt_file(file_path, receiver_public_key)
                signature = sign_encrypted_File(private_key_path, encrypted_file)
                ### db ###########

                ui_sendFile.show_info("File sent!")
                window_sendFile.close()


start_ui()
