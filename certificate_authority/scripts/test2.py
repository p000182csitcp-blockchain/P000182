from scripts.walletAccount import *


def main():
    # wallet account 5
    wallet_key5 = "bd8715cb599a70f56e113976831be145a9df246685e120222fd06060cf68b95d"
    # # get account
    wallet_account5 = get_wallet_account(wallet_key5)

    # # wallet account 6
    wallet_key6 = "8e4ac4cbdd15afb0191fd03f8ddc6508602fd8155e689f3a6c6c990762d499c6"
    # # get account
    wallet_account6 = get_wallet_account(wallet_key6)

    # get the most recent contract deployed
    certification = RSACertification[-1]

    # show certificate information
    user_name5 = certification.getUserName({"from": wallet_account6})

    # get the most recent contract deployed
    certification = RSACertification[-2]

    # show certificate information
    user_name6 = certification.getUserName({"from": wallet_account5})

    print(user_name5, user_name6)
