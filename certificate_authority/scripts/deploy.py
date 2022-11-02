from brownie import accounts, config, RSACertification, network
from scripts.walletAccount import get_wallet_account
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme


def deploy_certification(wallet_key):
    # get account
    wallet_account = get_wallet_account(wallet_key)

    # deploy RSA certificate smart contract
    certification = RSACertification.deploy({"from": wallet_account})


def create_certificate(wallet_key, user_name, email, phone, key_size, user_public_key):
    # get account
    wallet_account = get_wallet_account(wallet_key)

    # get the most recent contract deployed
    certification = RSACertification[-1]

    public_key_bytes_array = []
    if key_size == 1024:
        public_key_bytes_array.append(user_public_key[0:32])
        public_key_bytes_array.append(user_public_key[32:64])
        public_key_bytes_array.append(user_public_key[64:96])
        public_key_bytes_array.append(user_public_key[96:128])
        public_key_bytes_array.append(user_public_key[128:160])
        public_key_bytes_array.append(user_public_key[160:192])
        public_key_bytes_array.append(user_public_key[192:224])
        public_key_bytes_array.append(user_public_key[224:256])
        public_key_bytes_array.append(user_public_key[256:])
    elif key_size == 2048:
        public_key_bytes_array.append(user_public_key[0:32])
        public_key_bytes_array.append(user_public_key[32:64])
        public_key_bytes_array.append(user_public_key[64:96])
        public_key_bytes_array.append(user_public_key[96:128])
        public_key_bytes_array.append(user_public_key[128:160])
        public_key_bytes_array.append(user_public_key[160:192])
        public_key_bytes_array.append(user_public_key[192:224])
        public_key_bytes_array.append(user_public_key[224:256])
        public_key_bytes_array.append(user_public_key[256:288])
        public_key_bytes_array.append(user_public_key[288:320])
        public_key_bytes_array.append(user_public_key[320:352])
        public_key_bytes_array.append(user_public_key[352:384])
        public_key_bytes_array.append(user_public_key[384:416])
        public_key_bytes_array.append(user_public_key[416:448])
        public_key_bytes_array.append(user_public_key[448:])
    elif key_size == 3072:
        public_key_bytes_array.append(user_public_key[0:32])
        public_key_bytes_array.append(user_public_key[32:64])
        public_key_bytes_array.append(user_public_key[64:96])
        public_key_bytes_array.append(user_public_key[96:128])
        public_key_bytes_array.append(user_public_key[128:160])
        public_key_bytes_array.append(user_public_key[160:192])
        public_key_bytes_array.append(user_public_key[192:224])
        public_key_bytes_array.append(user_public_key[224:256])
        public_key_bytes_array.append(user_public_key[256:288])
        public_key_bytes_array.append(user_public_key[288:320])
        public_key_bytes_array.append(user_public_key[320:352])
        public_key_bytes_array.append(user_public_key[352:384])
        public_key_bytes_array.append(user_public_key[384:416])
        public_key_bytes_array.append(user_public_key[416:448])
        public_key_bytes_array.append(user_public_key[448:480])
        public_key_bytes_array.append(user_public_key[480:512])
        public_key_bytes_array.append(user_public_key[512:544])
        public_key_bytes_array.append(user_public_key[544:576])
        public_key_bytes_array.append(user_public_key[576:608])
        public_key_bytes_array.append(user_public_key[608:])

    print("[ Create", user_name, "'s certificate ]")

    transaction = certification.createCertificate(
        user_name,
        email,
        phone,
        key_size,
        public_key_bytes_array,
        {"from": wallet_account},
    )
    transaction.wait(1)
