from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class pemilahan_sampah(models.Model):
    _name="dashboard_web.pemilahan_sampah"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Nama Provinsi",required=True)
    kategori = fields.Selection([
        ('1', 'Dipilah dan sebagian dimanfaatkan'),
        ('2', 'Dipilah kemudian dibuang'),
        ('3','Tidak dipilah')
    ], string='Kategori', default='1',required=True)
    jenis = fields.Selection([
        ('8', 'Pemilahan Sampah')
    ], string='Jenis Survey', default='8',required=True)
    persentase = fields.Float(string="Persentase", digits=(12,1),required=True)