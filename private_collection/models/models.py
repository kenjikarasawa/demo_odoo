# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class private_collection(models.Model):
#     _name = 'private_collection.private_collection'
#     _description = 'private_collection.private_collection'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
