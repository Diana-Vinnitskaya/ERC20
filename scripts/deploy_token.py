from brownie import MyToken, accounts, network
from typing import List 

def main():
    
    
    amount_per_account = 100000 * 10**18

    accounts = ['0xC0BcE0346d4d93e30008A1FE83a2Cf8CfB9Ed301', '0xf414d65808f5f59aE156E51B97f98094888e7d92', '0x055f1c2c9334a4e57ACF2C4d7ff95d03CA7d6741', '0x1B63B4495934bC1D6Cb827f7a9835d316cdBB332', '0x303E8684b9992CdFA6e9C423e92989056b6FC04b', '0x5eC14fDc4b52dE45837B7EC8016944f75fF42209', '0x22162F0D8Fd490Bde6Ffc9425472941a1a59348a', '0x1DA0dcC27950F6070c07F71d1dE881c3C67CEAab', '0xa4c7f832254eE658E650855f1b529b2d01C92359','0x275CAe3b8761CEdc5b265F3241d07d2fEc51C0d8']
    initial_accounts = [accounts[0], accounts[1], accounts[2]]

    my_token = MyToken.deploy("My Token", "MTK", initial_accounts, amount_per_account, {"from": accounts[0]})
    print("Token deployed:", my_token)
    
    # Burn some tokens
    my_token.burn(50 * 10**18, {"from": accounts[0]})
    print("Burned 50 tokens from", accounts[0])

    # Transfer tokens
    my_token.transfer(accounts[1], 20 * 10**18, {"from": accounts[0]})
    print("Transferred 20 tokens from", accounts[0], "to", accounts[1])

    
