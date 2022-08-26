# -*- coding: utf-8 -*-
# from odoo import http


# class KkiProducts(http.Controller):
#     @http.route('/kki_products/kki_products/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_products/kki_products/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_products.listing', {
#             'root': '/kki_products/kki_products',
#             'objects': http.request.env['kki_products.kki_products'].search([]),
#         })

#     @http.route('/kki_products/kki_products/objects/<model("kki_products.kki_products"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_products.object', {
#             'object': obj
#         })
