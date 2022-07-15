
from brownie import GIT, accounts

def deploy():
    account = accounts[0]
    test = GIT.deploy(
        {"from": account},
    )

def main():
    deploy()

