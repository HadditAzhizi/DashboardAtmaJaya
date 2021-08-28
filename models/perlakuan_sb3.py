from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class perlakuan_sb3(models.Model):
    _name="dashboard_web.perlakuan_sb3"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Nama Provinsi",required=True)
    kategori = fields.Selection([
        ('1', 'Didaur ulang/diolah'),
        ('2', 'Dijual'),
        ('3','Lainnya')
    ], string='Kategori', default='1',required=True)
    jenis = fields.Selection([
        ('9', 'Perlakuan Sampah B3')
    ], string='Jenis Survey', default='9',required=True)
    persentase = fields.Float(string="Persentase", digits=(12,1),required=True)