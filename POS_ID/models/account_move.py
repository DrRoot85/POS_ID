# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'account.move'

    type = fields.Selection([('in_invoice', 'Lin_invoice'), ('in_refund', 'in_refund')], string='Type:')
