from Crypto.PublicKey import RSA


def generate_RSA_key_pairs(key_size):
    # Use RSA to generate user key pairs
    KeyPair = RSA.generate(bits=key_size)
    private_key = KeyPair.exportKey("PEM")
    public_key = KeyPair.publickey().exportKey("PEM")

    # # save PEM key as files
    # with open("file/private_key.pem", "wb") as file:
    #     file.write(private_key)

    return private_key, public_key
