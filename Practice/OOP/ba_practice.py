# -*- coding: utf-8 -*-
"""
Using the bank account made in bank_account.py

Note: you likely need to restart kernel to apply changes to bank_account.py
"""

from decimal import Decimal
from bank_account import Account

account1 = Account('JG', Decimal('20.00'))

account1.deposit(Decimal('10.00'))

account1.withdraw(Decimal('20.00'))

account1.withdraw(Decimal('50.00')) # errors on purpose

# enhance to unit tests
# test show_balance()
# test close()