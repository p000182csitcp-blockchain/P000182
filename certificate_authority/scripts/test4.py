from scripts.crypto import *
from scripts.walletAccount import *
from MongoDB.UserFactory import *

# receiver
wallet_key5 = "bd8715cb599a70f56e113976831be145a9df246685e120222fd06060cf68b95d"
# get account
wallet_account = get_wallet_account(wallet_key5)
# get the most recent contract deployed
certification = RSACertification[0]
# show certificate information
user_name = certification.getUserName({"from": wallet_account})
public_key_bytes_array = certification.getPublicKey({"from": wallet_account})
receiver_public_key = b""
for bt in public_key_bytes_array:
    receiver_public_key += bt


def main():
    # ef = encrypt_file("file/photo.jpg", receiver_public_key)
    # with open("C:/Users/Jakll/Desktop/file_to_save.bin", "wb") as fp:
    #     fp.write(ef)

    userFact = UserFactory()
    f_info = userFact.get_file_by_id("6367f3b808aa53335b794fd5")

    # decode the plain_file
    plain_file = base64.b64decode(f_info["file"])

    m_info = userFact._messages.find_one({"_id": ObjectId("6367f3b608aa53335b794fd4")})

    # verify file
    signed_file_succ = verify_file(
        m_info["signature"],
        plain_file,
        userFact.get_public_key("alice"),
        # get sender's key len
        userFact.get_key_len("alice"),
    )

    # with open("file/file_to_save.bin", "rb") as fr:
    #     file_read = fr.read()

    # decrypt_file(file_read, "1.jpg", "C:/Users/Jakll/Desktop/my_private_key.pem", 1024)
