// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, Ownable {
    
    constructor(
        string memory name,
        string memory symbol,
        address[] memory initial_accounts,
        uint256 initialAmount
    ) ERC20(name, symbol) {
        require(initial_accounts.length > 0, "At least one initial account required");
        require(initialAmount * initial_accounts.length <= 1000000 * 10 ** decimals(), "Exceeds total supply");
        
        for (uint256 i = 0; i < initial_accounts.length; i++) {
            _mint(initial_accounts[i], initialAmount);
        }
    }

    function mint(address account, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= 1000000 * 10 ** decimals(), "Exceeds total supply");
        _mint(account, amount);
    }

    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        return super.transfer(recipient, amount);
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(balanceOf(sender) >= amount, "Insufficient balance");
        return super.transferFrom(sender, recipient, amount);
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return super.allowance(owner, spender);
    }

    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }
}
