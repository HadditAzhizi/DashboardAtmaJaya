# -*- coding: utf-8 -*-
from odoo import http

class Dashboard(http.Controller):

    @http.route('/dashboard', auth='public', website=True)
    def index(self, **kw):
         self._cr.execute("SELECT * FROM dashboard_web_sumber_air")
         data = self._cr.dictfetchall()
         return http.request.render('dashboard_web.index', {
             'sumber_air': data
         })