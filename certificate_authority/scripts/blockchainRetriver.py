from brownie import accounts, config, RSACertification, network
from scripts.walletAccount import *


def getPublicKeyFromBlockchain(user_id, user_wallet_key):
    # get the contract deployed
    # get account
    wallet_account = get_wallet_account(user_wallet_key)
    certification = RSACertification[user_id]
    public_key_bytes_array = certification.getPublicKey({"from": wallet_account})
    print(public_key_bytes_array)
    public_key = b""
    for bt in public_key_bytes_array:
        public_key += bt

    return public_key


def main():
    print(
        getPublicKeyFromBlockchain(
            0, "bd8715cb599a70f56e113976831be145a9df246685e120222fd06060cf68b95d"
        )
    )
