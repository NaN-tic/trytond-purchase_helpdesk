# This file is part of the purchase_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import configuration
from . import helpdesk
from . import getmail


def register():
    Pool.register(
        configuration.HelpdeskConfiguration,
        helpdesk.Helpdesk,
        helpdesk.PurchaseHelpdesk,
        getmail.GetmailServer,
        module='purchase_helpdesk', type_='model')
