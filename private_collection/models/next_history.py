# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class private_collection_next_history(models.Model):
    _name = 'private_collection.history'
    _description = 'private_collection.history'

    name = fields.Char("name")
    check_date = fields.Date("check date", required=True, default=datetime.today())
    game_id = fields.Many2one("private_collection.collect", "Collection")
    image = fields.Binary("image")
    scratch_1 = fields.Boolean("傷はあるか")
    crease_1 = fields.Boolean("折れはあるか")
    desperation_1 = fields.Boolean("焼けはあるか")
    gouge_1 = fields.Boolean("ヘコミはあるか")
    break_1 = fields.Boolean("破れはあるか")
    peeling_off_1 = fields.Boolean("剥がれはあるか")

