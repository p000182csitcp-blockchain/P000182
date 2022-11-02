from inspect import signature
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5 as PK
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import zlib
import base64
from scripts.deploy import *
from scripts.walletAccount import *
import os


def get_private_key(private_key_path):
    # read the private key by using the path
    private_key_file = open(private_key_path, "rb")
    private_key = private_key_file.read()
    return private_key


# encrypt message
def encrypt_message(message, receiver_public_key):
    cipher = PKCS1_v1_5.new(RSA.importKey(receiver_public_key))
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, private_key_path):
    try:
        # read the private key by using the path
        private_key = get_private_key(private_key_path)
        # decrypt message
        decipher = PKCS1_v1_5.new(RSA.importKey(private_key))
        decrypted_message = decipher.decrypt(encrypted_message, None).decode()
        print("[ Encrypted message is decrypted ]")
    except:
        print("[ Invalid private key ]")
        return ""

    return decrypted_message


def sign_message(message, private_key_path):
    # hash the message
    digest = SHA256.new()
    digest.update(message.encode("utf-8"))
    try:
        # read the private key by using the path
        private_key = get_private_key(private_key_path)

        # sign the message by using sender's private key
        signer = PK.new(RSA.importKey(private_key))
        signature = signer.sign(digest)
        print("[ A message is signed ]")
    except:
        print("[ Invalid private key ]")
        return ""

    return signature


def verify_signature(message, signature, sender_public_key):
    # verify the signed message by using sender's public key
    verifier = PKCS115_SigScheme(RSA.importKey(sender_public_key))
    hash = SHA256.new(str.encode(message))
    try:
        # verify the signed message
        verifier.verify(hash, signature)
        print("[ Signature is valid. ]")
        return True
    except:
        print("[ Signature is Invalid. ]")
        return False


def sign_encrypted_message(encrypted_message, private_key_path):
    # hash the message
    digest = SHA256.new()
    digest.update(encrypted_message)
    try:
        # read the private key by using the path
        private_key = get_private_key(private_key_path)

        # sign the message by using sender's private key
        signer = PK.new(RSA.importKey(private_key))
        signature = signer.sign(digest)
        print("[ A message is signed ]")
    except:
        print("[ Invalid private key ]")
        return ""

    return signature


def verify_encryptedMessage(
    encrypted_message, encrypted_message_signature, sender_public_key
):
    # verify the signed message by using sender's public key
    verifier = PKCS115_SigScheme(RSA.importKey(sender_public_key))
    hash = SHA256.new(encrypted_message)
    try:
        # verify the signed message
        verifier.verify(hash, encrypted_message_signature)
        print("[ Signature is valid. ]")
        return True
    except:
        print("[ Signature is Invalid. ]")
        return False


# ref: https://ismailakkila.medium.com/black-hat-python-encrypt-and-decrypt-with-rsa-cryptography-bd6df84d65bc
def encrypt_blob(blob, receiver_public_key):
    # Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(receiver_public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    # compress the data first
    blob = zlib.compress(blob)

    # In determining the chunk size, determine the private key length used in bytes
    # and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    # in chunks
    chunk_size = 86
    offset = 0
    end_loop = False
    encrypted = b""

    while not end_loop:
        # The chunk
        chunk = blob[offset : offset + chunk_size]

        # If the data chunk is less then the chunk size, then we need to add
        # padding with " ". This indicates the we reached the end of the file
        # so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b" " * (chunk_size - len(chunk))

        # Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        # Increase the offset by chunk size
        offset += chunk_size

    print("[ The file is encrypted ]")
    # Base 64 encode the encrypted file
    return base64.b64encode(encrypted)


def decrypt_blob(encrypted_blob, private_key_path):
    # read the private key by using the path
    private_key = get_private_key(private_key_path)

    # Import the Private Key and use for decryption using PKCS1_OAEP
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    # Base 64 decode the data
    encrypted_blob = base64.b64decode(encrypted_blob)

    # In determining the chunk size, determine the private key length used in bytes.
    # The data will be in decrypted in chunks
    chunk_size = 128
    offset = 0
    decrypted = b""

    # keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        # The chunk
        chunk = encrypted_blob[offset : offset + chunk_size]

        # Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        # Increase the offset by chunk size
        offset += chunk_size

    # return the decompressed decrypted data
    return zlib.decompress(decrypted)


def sign_blob(blob, private_key):
    # compress the data first
    blob = zlib.compress(blob)

    # In determining the chunk size, determine the private key length used in bytes
    # and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    # in chunks
    chunk_size = 86
    offset = 0
    end_loop = False
    blob_signature = b""

    # sign the message by using sender's private key
    signer = PK.new(RSA.importKey(private_key))

    while not end_loop:
        # The chunk
        chunk = blob[offset : offset + chunk_size]
        digest = SHA256.new()
        digest.update(chunk)

        # If the data chunk is less then the chunk size, then we need to add
        # padding with " ". This indicates the we reached the end of the file
        # so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b" " * (chunk_size - len(chunk))

        # Append the encrypted chunk to the overall encrypted file
        blob_signature += signer.sign(digest)

        # Increase the offset by chunk size
        offset += chunk_size

    print("[ The file is signed ]")

    return blob_signature


def verify_blob(blob_signature, blob, sender_public_key):
    blob = zlib.compress(blob)

    # In determining the chunk size, determine the private key length used in bytes.
    # The data will be in decrypted in chunks
    chunk_size = 128
    offset = 0
    verification = True

    og_chunk_size = 86
    og_offset = 0

    verifier = PKCS115_SigScheme(RSA.importKey(sender_public_key))

    # keep loop going as long as we have chunks to decrypt
    while offset < len(blob_signature):
        # The chunk
        chunk = blob_signature[offset : offset + chunk_size]
        # The og chunk
        og_chunk = blob[og_offset : og_offset + og_chunk_size]

        hash = SHA256.new(og_chunk)
        try:
            # verify the signed message
            verifier.verify(hash, chunk)
        except:
            print("[ Signature is Invalid. ]")
            verification = False

        # Increase the offset by chunk size
        offset += chunk_size
        og_offset += og_chunk_size

    # return the decompressed decrypted data
    return verification


def encrypt_file(file_path, receiver_public_key):
    with open(file_path, "rb") as file:
        blob = file.read()

    return encrypt_blob(blob, receiver_public_key)


def decrypt_file(encrypted_file, file_name, private_key_path):
    try:
        # read the private key by using the path
        private_key = get_private_key(private_key_path)

        # decrypt file and save
        # print(os.getcwd())
        file_path = os.getcwd() + "\\" + file_name
        # print(filepath2)

        with open(file_path, "wb") as file:
            file.write(decrypt_blob(encrypted_file, private_key))

        print("[ Encrypted file is decrypted and saved]")
    except:
        print("[ Invalid private key ]")
        return ""


def sign_file(private_key_path, file_path):
    try:
        # read the private key by using the path
        private_key = get_private_key(private_key_path)

        with open(file_path, "rb") as file:
            blob = file.read()

        return sign_blob(blob, private_key)
    except:
        print("[ Invalid private key ]")
        return ""


def verify_file(blob_signature, blob, sender_public_key):
    return verify_blob(blob_signature, blob, sender_public_key)


def sign_encrypted_File(private_key_path, encrypted_file):
    try:
        # read the private key by using the path
        private_key = get_private_key(private_key_path)
        return sign_blob(encrypted_file, private_key)
    except:
        print("[ Invalid private key ]")
        return ""


def verify_encryptedFile(encrypted_file_signature, encrypted_file, sender_public_key):
    return verify_blob(encrypted_file_signature, encrypted_file, sender_public_key)
