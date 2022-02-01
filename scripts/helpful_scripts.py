from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENT = [
    "ganache",
    "local-ganache",
    "hardhat",
    "development",
    "mainnet-fork",
]


def get_account(id=None, index=None):
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    if network.show_active() in config["networks"]:
        return accounts.add(config["networks"]["from_key"])
    return None
