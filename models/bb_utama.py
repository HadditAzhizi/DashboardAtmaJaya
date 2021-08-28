from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class bb_utama(models.Model):
    _name="dashboard_web.bb_utama"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Nama Provinsi",required=True)
    kategori = fields.Selection([
        ('1', 'Listrik'),
        ('2', 'Gas Kota/Elpiji'),
        ('3', 'Biogas'),
        ('4', 'Minyak tanah'),
        ('5', 'Briket'),
        ('6', 'Arang'),
        ('7', 'Kayu bakar'),
        ('8', 'Lainnya'),
        ('9', 'Tidak memasak')
    ], string='Kategori', default='1',required=True)
    jenis = fields.Selection([
        ('6', 'Bahan Bakar Utama')
    ], string='Jenis Survey', default='6',required=True)
    persentase = fields.Float(string="Persentase", digits=(12,1),required=True)