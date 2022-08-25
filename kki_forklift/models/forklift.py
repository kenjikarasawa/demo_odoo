# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_forklift(models.Model):
    _name = 'kki_forklift.lift'
    _description = 'kki_forklift.lift'

    name = fields.Char("name")
    image = fields.Binary("image")
    launch_day = fields.Date("launch_day")
    vendor = fields.Many2one("res.partner", string="vendor")
    size = fields.Many2one("kki_forklift.size", string="size")
    note = fields.Text("note")
    check_history_ids = fields.One2many(
        comodel_name="kki_forklift.history",
        inverse_name="lift_id",
        string="check history")

    # Integerは空の場合0が入る
    price = fields.Integer("price")
    # これ（store=True）を入れるとデータベースにtaxの記録が残る
    tax = fields.Float("tax", compute="_get_tax", store=True, Tracking=True)

    # これ(@api.depends)を入れるとデータベースにtaxの記録が残る
    @api.depends("price")
    # selfは画面の値を全て拾ってきてしまう
    # この自動計算の場合は値がOdoo上に記録されない（デフォルトでは）
    def _get_tax(self):
        for rec in self:
            if rec.price:

                tax = rec.price * 0.1
                # これでtaxの値が項目に渡る
                rec.tax = tax
            else:
            # 例外の場合は0を入れる
                rec.tax = 0

