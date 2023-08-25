import pytest
from brownie import MyToken, accounts

@pytest.fixture(scope="module")
def token():
    initial_holders = [accounts[1], accounts[2], accounts[3]]
    token = MyToken.deploy("MyToken", "MTK", initial_holders, 100000, {"from": accounts[0]})
    yield token

def test_deploy(token):
    assert token.name() == "MyToken"
    assert token.symbol() == "MTK"
    assert token.totalSupply() == 300000

def test_mint(token):
    mint_amount = 100000
    token.mint(accounts[2], mint_amount, {"from": accounts[0]})
    assert token.totalSupply() == 400000
    assert token.balanceOf(accounts[1]) == mint_amount

def test_burn(token):
    assert token.balanceOf(accounts[1]) >= 50
    burn_amount = 50
    initial_balance = token.balanceOf(accounts[1])
    token.burn(burn_amount, {"from": accounts[1]})
    assert token.balanceOf(accounts[1]) == initial_balance - burn_amount

def test_approve_transfer(token):
    assert token.balanceOf(accounts[0]) >= 50
    assert token.balanceOf(accounts[1]) >= 50
    assert token.balanceOf(accounts[2]) >= 50

def test_approve_transfer(token):
    token.approve(accounts[0], 500000)
    token.approve(accounts[1], 500000)
    assert token.allowance(accounts[0], accounts[1]) == 500000
    initial_balance_sender = token.balanceOf(accounts[0])
    initial_balance_recipient = token.balanceOf(accounts[1])
    amount_to_transfer = 30
    assert initial_balance_sender >= amount_to_transfer, "Insufficient balance for sender"
    assert initial_balance_recipient + amount_to_transfer <= 1000000 * 10 ** 18, "Total supply exceeded"
    token.transferFrom(accounts[0], accounts[1], amount_to_transfer, {"from": accounts[0]})
    assert token.balanceOf(accounts[0]) == initial_balance_sender - amount_to_transfer
    expected_balance_recipient = initial_balance_recipient + amount_to_transfer
    assert token.balanceOf(accounts[1]) == expected_balance_recipient


def test_transfer(token):
    assert token.balanceOf(accounts[0]) >= 20
    initial_balance_sender = token.balanceOf(accounts[0])
    initial_balance_recipient = token.balanceOf(accounts[1])
    transfer_amount = 10
    token.transfer(accounts[1], transfer_amount, {"from": accounts[0]})
    assert token.balanceOf(accounts[0]) == initial_balance_sender - transfer_amount
    assert token.balanceOf(accounts[1]) == initial_balance_recipient + transfer_amount


