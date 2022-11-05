from brownie import accounts, config, RSACertification, network


def get_public_key(user_id, user_wallet_key):
    # get the contract deployed
    certification = RSACertification[user_id - 1]
    public_key = certification.getPublicKey({"from": user_wallet_key})
    return public_key
