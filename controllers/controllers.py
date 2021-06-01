# -*- coding: utf-8 -*-
from odoo import http


class toka2(http.Controller):
    @http.route('/toka2/toka2/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/toka2/toka2/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('toka2.listing', {
            'root': '/toka2/toka2',
            'objects': http.request.env['toka2.toka2'].search([]),
        })

    @http.route('/toka2/toka2/objects/<model("toka2.toka2"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('toka2.object', {
            'object': obj
        })
