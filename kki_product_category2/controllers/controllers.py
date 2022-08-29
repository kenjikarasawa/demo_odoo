# -*- coding: utf-8 -*-
# from odoo import http


# class KkiProductCategory2(http.Controller):
#     @http.route('/kki_product_category2/kki_product_category2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_product_category2/kki_product_category2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_product_category2.listing', {
#             'root': '/kki_product_category2/kki_product_category2',
#             'objects': http.request.env['kki_product_category2.kki_product_category2'].search([]),
#         })

#     @http.route('/kki_product_category2/kki_product_category2/objects/<model("kki_product_category2.kki_product_category2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_product_category2.object', {
#             'object': obj
#         })
