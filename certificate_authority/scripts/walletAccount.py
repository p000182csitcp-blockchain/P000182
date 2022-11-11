from brownie import accounts, config, RSACertification, network


def get_wallet_account(wallet_key):
    if network.show_active() == "development":
        # blockchain account provided by Ganache-cli
        return accounts[0]
    else:
        # return metamask wallet account using wallet_key
        return accounts.add(wallet_key)
