# -*- coding: utf-8 -*-
# from odoo import http


# class KkiSale(http.Controller):
#     @http.route('/kki_sale/kki_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_sale/kki_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_sale.listing', {
#             'root': '/kki_sale/kki_sale',
#             'objects': http.request.env['kki_sale.kki_sale'].search([]),
#         })

#     @http.route('/kki_sale/kki_sale/objects/<model("kki_sale.kki_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_sale.object', {
#             'object': obj
#         })
