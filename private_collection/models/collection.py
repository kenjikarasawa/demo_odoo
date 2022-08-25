# -*- coding: utf-8 -*-

from odoo import models, fields, api


class private_collection(models.Model):
    _name = 'private_collection.collect'
    _description = 'private_collection.collect'

    name = fields.Char("name")
    image = fields.Binary("image")
    release_date = fields.Date("release_date")
    company = fields.Many2one("res.partner", string="company")
    condition = fields.Selection([
        ("1", "新古品"),
        ("2", "使用感少なめ"),
        ("3", "使用感あり"),
        ("4", "使用感・汚れあり")
    ], default="", string="condition")
    next_history_ids = fields.One2many(
        comodel_name="private_collection.history",
        inverse_name="game_id",
        string="Collection")

