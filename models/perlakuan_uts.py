from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class perlakuan_uts(models.Model):
    _name="dashboard_web.perlakuan_uts"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Nama Provinsi",required=True)
    kategori = fields.Selection([
        ('1', 'Didaur ulang'),
        ('2', 'Dibuat kompos/pupuk'),
        ('3', 'Diangkut petugas/dibuang ke TPS/TPA'),
        ('4', 'Dijual ke pengumpul barang bekas'),
        ('5', 'Ditimbun/dikubur'),
        ('6', 'Dibakar'),
        ('7', 'Dibuang ke laut/sungai/got'),
        ('8', 'Dibuang sembarangan'),
        ('9', 'Dijadikan makanan ternak'),
        ('99','Lainnya')
    ], string='Kategori', default='1',required=True)
    jenis = fields.Selection([
        ('10', 'Perlakuan Utama Terhadap Sampah')
    ], string='Jenis Survey', default='10',required=True)
    persentase = fields.Float(string="Persentase", digits=(12,1),required=True)