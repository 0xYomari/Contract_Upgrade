from scripts.helpful_scripts import get_account
from brownie import network, Box, ProxyAdmin


def main():
    account = get_account()
    print(f"Devloping to {network.show_active()}")
    box = Box.deploy({"from": account})

    proxy_admin = ProxyAdmin.deploy({"from": account})
