# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo import http
from odoo.http import request
import logging
import json

_logger = logging.getLogger(__name__)
class fungsi():	
    
    @api.model
    def ktg_smb_air(self, val):
    	kategori = ""
    	if val=='1':kategori = "Air kemasan/ air isi ulang"
    	elif val=='2':kategori = "Leding"
    	elif val=='3':kategori = "Sumur bor/ pompa"
    	elif val=='4':kategori = "Sumur terlindung"
    	elif val=='5':kategori = "Sumur tidak terlindung"
    	elif val=='6':kategori = "Mata air terlindung"
    	elif val=='7':kategori = "Mata air tidak terlindung"
    	elif val=='8':kategori = "Air sungai"
    	elif val=='9':kategori = "Waduk/danau"
    	elif val=='10':kategori = "Air hujan"
    	elif val=='99':kategori = "Tidak ada Jawaban"
    	return kategori    

    @api.model
    def jenis_smb_air(self, val):
    	jenis = ""
    	if val=='1':jenis = "Sumber air cuci baju"
    	elif val=='2':jenis = "Sumber air cuci kendaraan"
    	elif val=='3':jenis = "Sumber air mandi"
    	elif val=='4':jenis = "Sumber air masak"
    	elif val=='5':jenis = "Sumber air minum"
    	return jenis

    @api.model
    def ktg_bb_utama(self, val):
    	jenis = ""
    	if val=='1':jenis = "Listrik"
    	elif val=='2':jenis = "Gas Kota/Elpiji"
    	elif val=='3':jenis = "Biogas"
    	elif val=='4':jenis = "Minyak tanah"
    	elif val=='5':jenis = "Briket"
    	elif val=='6':jenis = "Arang"
    	elif val=='7':jenis = "Kayu bakar"
    	elif val=='8':jenis = "Lainnya"
    	elif val=='9':jenis = "Tidak memasak"
    	return jenis

    @api.model
    def ktg_bb_cadangan(self, val):
        jenis = ""
        if val=='1':jenis = "Listrik PLN"
        elif val=='2':jenis = "Listrik non PLN bersumber energi alternatif"
        elif val=='3':jenis = "Listrik non PLN bukan bersumber energi alternatif"
        elif val=='4':jenis = "Petromak/pelita/sentir/obor"
        elif val=='5':jenis = "Lainnya"
        return jenis
        
    @api.model
    def ktg_pemil_sampah(self, val):
        jenis = ""
        if val=='1':jenis = "Dipilah dan sebagian dimanfaatkan"
        elif val=='2':jenis = "Dipilah kemudian dibuang"
        elif val=='3':jenis = "Tidak dipilah"
        return jenis

    @api.model
    def ktg_perlakuan_sb3(self, val):
        jenis = ""
        if val=='1':jenis = "Didaur ulang/diolah"
        elif val=='2':jenis = "Dijual"
        elif val=='3':jenis = "Lainnya"
        return jenis

    @api.model
    def ktg_perlakuan_uts(self, val):
        jenis = ""
        if val=='1':jenis = "Didaur ulang"
        elif val=='2':jenis = "Dibuat kompos/pupuk"
        elif val=='3':jenis = "Diangkut petugas/dibuang ke TPS/TPA"
        elif val=='4':jenis = "Dijual ke pengumpul barang bekas"
        elif val=='5':jenis = "Ditimbun/dikubur"
        elif val=='6':jenis = "Dibakar"
        elif val=='7':jenis = "Dibuang ke laut/sungai/got"
        elif val=='8':jenis = "Dibuang sembarangan"
        elif val=='9':jenis = "Dijadikan makanan ternak"
        elif val=='99':jenis = "Lainnya"
        return jenis

    @api.model
    def ktg_sumber_pu(self, val):
        jenis = ""
        if val=='1':jenis = "Listrik PLN"
        elif val=='2':jenis = "Listrik non PLN bersumber energi alternatif"
        elif val=='3':jenis = "Listrik non PLN bukan bersumber energi alternatif"
        elif val=='4':jenis = "Petromak/pelita/sentir/obor"
        elif val=='5':jenis = "Lainnya"
        return jenis

class Dashboard(http.Controller):

    @http.route('/dashboard', auth='public', website=True)
    def index(self, **kw):
         return http.request.render('dashboard_web.index', {
         })

    @http.route('/get_sumber_air', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_sumber_air(self, **kw):
    	id_prov = kw.get('id_prov')
    	id_jenis = kw.get('id_jenis')

    	if id_jenis=="":
    		request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_sumber_air as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND kategori != '99' order by jenis, persentase desc")
    	else:
    		request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_sumber_air as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND jenis = '"+str(id_jenis)+"' AND kategori != '99' order by jenis, persentase desc")	
    	
    	result = request.cr.dictfetchall()
    	data = []
    	for x in result:
    		data.append({
		        "provinsi": x.get('Nama_Provinsi'),
		        "persentase": x.get('persentase'),
		        "id_jenis": x.get('jenis'),
		        "jenis": fungsi.jenis_smb_air(self,x.get('jenis')),
		        "kategori": "Berasal dari "+fungsi.ktg_smb_air(self,x.get('kategori'))
		    })
    	# _logger.error("dashboard log : %r", result)
    	return json.dumps(data)

    @http.route('/get_bb_utama', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_bb_utama(self, **kw):
    	id_prov = kw.get('id_prov')
    	id_jenis = kw.get('id_jenis')

    	request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_bb_utama as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND jenis = '"+str(id_jenis)+"' AND kategori != '9' order by jenis, persentase desc")	
    	
    	result = request.cr.dictfetchall()
    	data = []
    	for x in result:
    		data.append({
		        "provinsi": x.get('Nama_Provinsi'),
		        "persentase": x.get('persentase'),
		        "id_jenis": x.get('jenis'),
		        "jenis": "Bahan Bakar Utama",
		        "kategori": "menunjukan penduduknya menggunakan "+fungsi.ktg_bb_utama(self,x.get('kategori'))
		    })
    	# _logger.error("dashboard log : %r", result)
    	return json.dumps(data)

    @http.route('/get_bb_cadangan', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_bb_cadangan(self, **kw):
    	id_prov = kw.get('id_prov')
    	id_jenis = kw.get('id_jenis')

    	request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_bb_cadangan as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND jenis = '"+str(id_jenis)+"' AND kategori != '5' order by jenis, persentase desc")	
    	
    	result = request.cr.dictfetchall()
    	data = []
    	for x in result:
    		data.append({
		        "provinsi": x.get('Nama_Provinsi'),
		        "persentase": x.get('persentase'),
		        "id_jenis": x.get('jenis'),
		        "jenis": "Bahan Bakar Cadangan",
		        "kategori": "menunjukan penduduknya menggunakan "+fungsi.ktg_bb_cadangan(self,x.get('kategori'))
		    })
    	# _logger.error("dashboard log : %r", result)
    	return json.dumps(data)

    @http.route('/get_pemilahan_sampah', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_pemilahan_sampah(self, **kw):
        id_prov = kw.get('id_prov')
        id_jenis = kw.get('id_jenis')

        request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_pemilahan_sampah as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND jenis = '"+str(id_jenis)+"' AND kategori != '3' order by jenis, persentase desc")   
        
        result = request.cr.dictfetchall()
        data = []
        for x in result:
            data.append({
                "provinsi": x.get('Nama_Provinsi'),
                "persentase": x.get('persentase'),
                "id_jenis": x.get('jenis'),
                "jenis": "Pemilahan Sampah",
                "kategori": "memilah sampah dengan cara "+fungsi.ktg_pemil_sampah(self,x.get('kategori'))
            })
        # _logger.error("dashboard log : %r", result)
        return json.dumps(data)

    @http.route('/get_perlakuan_sb3', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_perlakuan_sb3(self, **kw):
        id_prov = kw.get('id_prov')
        id_jenis = kw.get('id_jenis')

        request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_perlakuan_sb3 as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND jenis = '"+str(id_jenis)+"' AND kategori != '3' order by jenis, persentase desc")   
        
        result = request.cr.dictfetchall()
        data = []
        for x in result:
            data.append({
                "provinsi": x.get('Nama_Provinsi'),
                "persentase": x.get('persentase'),
                "id_jenis": x.get('jenis'),
                "jenis": "Mengolah Sampah B3",
                "kategori": "mengolah sampah B3 dengan cara "+fungsi.ktg_perlakuan_sb3(self,x.get('kategori'))
            })
        # _logger.error("dashboard log : %r", result)
        return json.dumps(data)

    @http.route('/get_perlakuan_uts', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_perlakuan_uts(self, **kw):
        id_prov = kw.get('id_prov')
        id_jenis = kw.get('id_jenis')

        request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_perlakuan_uts as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND jenis = '"+str(id_jenis)+"' AND kategori != '99' order by jenis, persentase desc")   
        
        result = request.cr.dictfetchall()
        data = []
        for x in result:
            data.append({
                "provinsi": x.get('Nama_Provinsi'),
                "persentase": x.get('persentase'),
                "id_jenis": x.get('jenis'),
                "jenis": "Mengolah Sampah",
                "kategori": "mengolah sampah dengan cara "+fungsi.ktg_perlakuan_uts(self,x.get('kategori'))
            })
        # _logger.error("dashboard log : %r", result)
        return json.dumps(data)

    @http.route('/get_sumber_pu', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_sumber_pu(self, **kw):
        id_prov = kw.get('id_prov')
        id_jenis = kw.get('id_jenis')

        request.cr.execute("SELECT DISTINCT ON (jenis) * FROM dashboard_web_sumber_pu as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where provinsi = '"+str(id_prov)+"' AND jenis = '"+str(id_jenis)+"' AND kategori != '5' order by jenis, persentase desc")   
        
        result = request.cr.dictfetchall()
        data = []
        for x in result:
            data.append({
                "provinsi": x.get('Nama_Provinsi'),
                "persentase": x.get('persentase'),
                "id_jenis": x.get('jenis'),
                "jenis": "Menggunakan",
                "kategori": "menggunakan "+fungsi.ktg_sumber_pu(self,x.get('kategori'))+" sebagai sumber penerangan utama"
            })
        # _logger.error("dashboard log : %r", result)
        return json.dumps(data)

    @http.route('/get_map', type='http', auth="public", website=False, methods=['POST','GET'], csrf=False)
    def get_map(self, **kw):
    	request.cr.execute("SELECT DISTINCT ON (kategori, provinsi) * FROM dashboard_web_sumber_air as a inner join dashboard_web_provinsi as b on a.provinsi=b.id  where kategori = '10' AND kategori != '99' order by kategori,provinsi, persentase desc")
    	result = request.cr.dictfetchall()
    	data = ""
    	hasil = []
    	color = "#bfbfbf"
    	for x in result:
    		idmap = x.get('Id_map')
    		dtmap = fungsi.jenis_smb_air(self,x.get('jenis'))+" pada provinsi "+x.get('Nama_Provinsi')+" menunjukan "+str(x.get('persentase'))+"% Berasal dari "+fungsi.ktg_smb_air(self,x.get('kategori'))
    		hasil.append([""+idmap+"",""+dtmap+"",""+color+""])
    	_logger.error("Data map log : %r", hasil)
    	return json.dumps(hasil)