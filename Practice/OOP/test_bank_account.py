# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:08:21 2026

@author: kolst
"""

import unittest
from decimal import Decimal
from bank_account import Account, to_decimal

unittest.main(verbosity=2)

class TestToDecimal(unittest.TestCase):
    """Tests for the standalone to_decimal helper function"""

    def test_decimal_passthrough(self):
        self.assertEqual(to_decimal(Decimal('50.00')), Decimal('50.00'))

    def test_int_conversion(self):
        self.assertEqual(to_decimal(100), Decimal('100'))

    def test_float_conversion(self):
        self.assertEqual(to_decimal(0.1), Decimal('0.1'))

    def test_string_conversion(self):
        self.assertEqual(to_decimal('75.10'), Decimal('75.10'))

    def test_invalid_string_raises(self):
        with self.assertRaises(Exception):
            to_decimal('not_a_number')


''' Notes for unit test code from package unittest:
TestCase.run() looks for something called setUp() to run before all tests
TestLoader runs anything that starts with test_
'''

class TestAccount(unittest.TestCase):

    def setUp(self):
        """Runs before every test method — gives each test a fresh account"""
        self.account = Account('High Roller', Decimal('100.00'))

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, Decimal('100.00'))

    def test_negative_initial_balance_raises(self):
        with self.assertRaises(ValueError):
            Account('High Roller', Decimal('-50.00'))

    def test_deposit_increases_balance(self):
        self.account.deposit(Decimal('25.00'))
        self.assertEqual(self.account.balance, Decimal('125.00'))

    def test_negative_deposit_raises(self):
        with self.assertRaises(ValueError):
            self.account.deposit(Decimal('-10.00'))

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(Decimal('40.00'))
        self.assertEqual(self.account.balance, Decimal('60.00'))

    def test_overdraft_raises(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(Decimal('200.00'))

    def test_close_with_zero_balance(self):
        self.account.withdraw(Decimal('100.00'))  # drain to zero
        self.account.close()
        self.assertEqual(self.account.is_open, False)

    def test_close_with_nonzero_balance_raises(self):
        with self.assertRaises(ValueError):
            self.account.close()


if __name__ == '__main__':
    unittest.main()