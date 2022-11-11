from brownie import accounts, config, RSACertification, network
from scripts.walletAccount import *


def getPublicKeyFromBlockchain(user_id, user_wallet_key):
    # get the contract deployed
    # get account
    wallet_account = get_wallet_account(user_wallet_key)
    for index in range(0, len(RSACertification)):
        certification = RSACertification[index]
        public_key_bytes_array = certification.getPublicKey(
            {"from": wallet_account})
        if public_key_bytes_array:
            # if not empty
            public_key = b""
            for bt in public_key_bytes_array:
                public_key += bt
            return public_key

    return b""
