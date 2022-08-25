# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_sale(models.Model):
    _inherit = 'sale.order'

    memo = fields.Text(string="メモ")
    x_time = fields.Datetime(string="発注日時")
    x_int = fields.Integer("販売数")
    x_slection = fields.Selection([
        ('1', '在庫無'),
        ('2', '在庫有'),
    ], default='',
        string="在庫", )
    x_m2o = fields.Many2one("res.partner", string="顧客名")
    note = fields.Char(string="note")
#     _name = 'kki_sale.kki_sale'
#     _description = 'kki_sale.kki_sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
