from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class pplh(models.Model):
    _name="dashboard_web.pplh"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Nama Provinsi",required=True)
    kategori = fields.Selection([
        ('1', 'Benar'),
        ('2', 'Salah'),
        ('9', 'Tidak tahu')
    ], string='Kategori', default='1', required=True)
    jenis = fields.Selection([
        ('1', 'Sumber air cuci baju'),
        ('2', 'Sumber air cuci kendaraan'),
        ('3', 'Sumber air mandi'),
        ('4', 'Sumber air masak'),
        ('5', 'Sumber air minum'),
        ('5', 'Sumber air minum'),
        ('5', 'Sumber air minum'),
        ('5', 'Sumber air minum'),
        ('5', 'Sumber air minum'),
        ('5', 'Sumber air minum'),
        ('5', 'Sumber air minum'),
        ('5', 'Sumber air minum')
    ], string='Jenis Survey', default='1', required=True)
    persentase = fields.Float(string="Persentase", digits=(12,1), required=True)