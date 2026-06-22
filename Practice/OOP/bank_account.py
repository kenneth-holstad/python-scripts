# -*- coding: utf-8 -*-
"""
Basic classes and methods for bank accounts
Adapted from Deitel intro OOP example
Added many new features like decimal conversion, is_open
"""

from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def to_decimal(amount):
    """Convert user inputs to decimal values"""
    if isinstance(amount, Decimal):
        return amount
    return Decimal(str(amount))

class Account:
    """Account class for maintaining a bank account name and balance"""
    
    def __init__(self, name, balance):
        """Initialize a bank account object"""
        balance = to_decimal(balance)
        
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance cannot be less than 0')
        
        self.name = name
        self.balance = balance
        self.is_open = True
        
        logger.info('Account initialized for %s with balance $%s', name, balance)
        
    def deposit(self, amount):
        """Add money to the account"""
        amount = to_decimal(amount)
        
        if amount < Decimal('0.00'):
            raise ValueError('Deposit amount must be positive')
            
        self.balance += amount
        
        logger.info('%s deposited $%s - new balance $%s', self.name, amount, self.balance)
        
    def withdraw(self, amount):
        """Withdraw money from the account"""
        amount = to_decimal(amount)
        
        if amount < Decimal('0.00'):
            raise ValueError('Withdrawal amount must be positive')
        
        if amount > self.balance:
            raise ValueError(f'Cannot overdraft the account. You have ${self.balance} available')
        
        self.balance -= amount
        
        logger.info('%s withdrew $%s - new balance $%s', self.name, amount, self.balance)
        
    def show_balance(self):
        """Return current balance in the account"""
        
        # unlike others this is intended to return to terminal
        print(f'{self.name} has a balance of ${self.balance}')
        
    def close(self):
        """Close account. Must have zero balance to proceed."""
        
        # change to requiring 0 - maybe I'll enable overdrafts at some point
        if self.balance != 0:
            raise ValueError(f'Must have 0 balance to close account. Current balance is ${self.balance}.')
        
        self.is_open = False
        
        logger.info('Account for %s has been closed successfully.', self.name)