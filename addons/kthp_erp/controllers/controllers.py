# -*- coding: utf-8 -*-
# from odoo import http


# class KthpErp(http.Controller):
#     @http.route('/kthp_erp/kthp_erp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kthp_erp/kthp_erp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kthp_erp.listing', {
#             'root': '/kthp_erp/kthp_erp',
#             'objects': http.request.env['kthp_erp.kthp_erp'].search([]),
#         })

#     @http.route('/kthp_erp/kthp_erp/objects/<model("kthp_erp.kthp_erp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kthp_erp.object', {
#             'object': obj
#         })
