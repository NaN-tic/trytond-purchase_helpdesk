# This file is part of the purchase_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PurchaseHelpdeskTestCase(ModuleTestCase):
    'Test Purchase Helpdesk module'
    module = 'purchase_helpdesk'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PurchaseHelpdeskTestCase))
    return suite
