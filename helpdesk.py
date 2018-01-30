# This file is part of the purchase_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Helpdesk', 'PurchaseHelpdesk']


class Helpdesk:
    __metaclass__ = PoolMeta
    __name__ = 'helpdesk'
    purchases = fields.Many2Many('purchase.purchase.helpdesk', 'helpdesk', 'purchase',
        'Purchases', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['purchase', 'generic']),
            },
        depends=['state', 'kind'])

    @classmethod
    def __setup__(cls):
        super(Helpdesk, cls).__setup__()
        value = ('purchase', 'Purchase')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)

    @classmethod
    def view_attributes(cls):
        return super(Helpdesk, cls).view_attributes() + [
            ('//page[@id="purchase"]', 'states', {
                    'invisible': ~Eval('kind').in_(['purchase', 'generic']),
                    })]


class PurchaseHelpdesk(ModelSQL):
    'Purchase - Helpdesk'
    __name__ = 'purchase.purchase.helpdesk'
    _table = 'purchase_purchase_helpdesk_rel'
    purchase = fields.Many2One('purchase.purchase', 'Purchase', ondelete='CASCADE',
        select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)
