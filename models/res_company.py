# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    x_nat_no = fields.Char(string="Nat ID/IQama")
