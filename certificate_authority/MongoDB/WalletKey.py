class WalletKey:
    def __init__(self) -> None:
        key_list = {
            # start with 5
            "0": "bd8715cb599a70f56e113976831be145a9df246685e120222fd06060cf68b95d",
            "1": "8e4ac4cbdd15afb0191fd03f8ddc6508602fd8155e689f3a6c6c990762d499c6",
            "2": "cc7144ed7103941beef293b8b4be7f2b300e85a6eac920b1062d4d65d3533143",
            "3": "14ed80e385c55297a9eb9a1e21612632ea2c81f01383d9eb18c5786bbabb9e72",
            "4": "27b2614a78c6304035aafeb5d208e6ddcea8b7a44ad2e142d8828d6436104748",
            "5": "e240fa32e02d384de67be40ebb989ed9bc05d296d68da11fe85c35710523e2aa",
            "6": "fd1ae9e6fe859c6c6129bb58856e003d7ade1de69ea8fec2f10a748ac26084af",
            "7": "f3a31919432c44dff27916f858577f5fa39ee54c86565e1c0f47c081a59d8b0e",
            "8": "8065b842e6f6dc4bcf6047ec0c08da60e8d1038019da3ad0941111e331bd8b86",
            "9": "6b271473e35f552793cb2edd83cdfd037e2aa7eb1bcf332e3825e3b3f0251616",
        }
        self._wallet_key_list = key_list

    def get_wallet_by_index(self, index):
        i = str(index)
        return self._wallet_key_list[i]
