# -*- coding: utf-8 -*-
# from odoo import http


# class PrivateCollection(http.Controller):
#     @http.route('/private_collection/private_collection/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/private_collection/private_collection/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('private_collection.listing', {
#             'root': '/private_collection/private_collection',
#             'objects': http.request.env['private_collection.private_collection'].search([]),
#         })

#     @http.route('/private_collection/private_collection/objects/<model("private_collection.private_collection"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('private_collection.object', {
#             'object': obj
#         })
