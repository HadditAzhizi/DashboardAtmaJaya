from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class Sumber_air(models.Model):
    _name="dashboard_web.sumber_air"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Nama Provinsi",required=True)
    kategori = fields.Selection([
        ('1', 'Air kemasan/ air isi ulang'),
        ('2', 'Leding '),
        ('3', 'Sumur bor/ pompa'),
        ('4', 'Sumur terlindung'),
        ('5', 'Sumur tidak terlindung'),
        ('6', 'Mata air terlindung'),
        ('7', 'Mata air tidak terlindung'),
        ('8', 'Air sungai'),
        ('9', 'Waduk/danau '),
        ('10', 'Air hujan'),
        ('99', 'Tidak ada Jawaban')
    ], string='Kategori', default='1')
    jenis = fields.Selection([
        ('1', 'Sumber air cuci baju'),
        ('2', 'Sumber air cuci kendaraan '),
        ('3', 'Sumber air mandi'),
        ('4', 'Sumber air masak'),
        ('5', 'Sumber air minum')
    ], string='Jenis Survey', default='1')
    persentase = fields.Char(String="Persentase")