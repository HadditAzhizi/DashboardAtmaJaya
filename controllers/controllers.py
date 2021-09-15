# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo import http
from odoo.http import request
import logging
import json

_logger = logging.getLogger(__name__)
# class fungsi():	 

class Dashboard(http.Controller):

    @http.route('/dashboard', auth='public', website=True)
    def index(self, **kw):
         return http.request.render('dashboard_web.index', {
         })

    @http.route('/get_config', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_config(self, **kw):
        request.cr.execute("SELECT * FROM dashboard_web_jenis_survey where is_publish='1'")
        result = request.cr.dictfetchall()
        data = []
        for x in result:
            data.append({
                "id_jenis": x.get('id'),
                "jenis_survey": x.get('nama')
            })
        return json.dumps(data)
         
    @http.route('/get_map', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_map(self, **kw):
        request.cr.execute("SELECT * FROM dashboard_web_provinsi")
        result = request.cr.dictfetchall()
        data = ""
        hasil = []
        color = "#bfbfbf"
        for x in result:
            hasil.append([""+str(x.get('Id_map'))+"",""+color+"",""+str(x.get('id'))+""])
        return json.dumps(hasil)
         
    @http.route('/post_data', type='http', auth="public", website=False, methods=['POST'], csrf=False)
    def post_data(self, **kw):
        id_prov = kw.get('id_prov')
        id_jenis = kw.get('id_jenis')[1:-1]
        if id_jenis!="":
            request.cr.execute("SELECT DISTINCT ON (a.survey) *,d.nama as survey,e.nama as kategori,a.survey as id_survey FROM dashboard_web_survey as a  inner join dashboard_web_isi_survey as c on a.id = c.survey inner join dashboard_web_provinsi as b on c.provinsi=b.id inner join dashboard_web_jenis_survey as d on a.survey=d.id inner join dashboard_web_kategori_survey as e on e.id = c.kategori where c.provinsi = '"+str(id_prov)+"' AND a.survey IN ("+id_jenis+") and d.is_publish = '1' and e.is_seleksi = '1' order by a.survey, c.persentase desc")
        else:
            request.cr.execute("SELECT DISTINCT ON (a.survey) *,d.nama as survey,e.nama as kategori,a.survey as id_survey FROM dashboard_web_survey as a  inner join dashboard_web_isi_survey as c on a.id = c.survey inner join dashboard_web_provinsi as b on c.provinsi=b.id inner join dashboard_web_jenis_survey as d on a.survey=d.id inner join dashboard_web_kategori_survey as e on e.id = c.kategori where c.provinsi = '"+str(id_prov)+"' and d.is_publish = '1' and e.is_seleksi = '1' order by a.survey, c.persentase desc")
        
        result = request.cr.dictfetchall()
        data = []
        for x in result:
            data.append({
                "provinsi": x.get('Nama_Provinsi'),
                "persentase": x.get('persentase'),
                "id_jenis": x.get('id_survey'),
                "jenis": x.get('survey'),
                "isi": x.get('template')+" "+x.get('kategori')
            })
        # _logger.error("dashboard log : %r", result)
        return json.dumps(data)