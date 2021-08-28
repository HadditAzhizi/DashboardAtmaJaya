from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class sumber_pu(models.Model):
    _name="dashboard_web.sumber_pu"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Nama Provinsi",required=True)
    kategori = fields.Selection([
        ('1', 'Listrik PLN'),
        ('2', 'Listrik non PLN bersumber energi alternatif'),
        ('3','Listrik non PLN bukan bersumber energi alternatif'),
        ('4','Petromak/pelita/sentir/obor'),
        ('5','Lainnya')
    ], string='Kategori', default='1',required=True)
    jenis = fields.Selection([
        ('11', 'Sumber Penerangan Utama')
    ], string='Jenis Survey', default='11',required=True)
    persentase = fields.Float(string="Persentase", digits=(12,1),required=True)