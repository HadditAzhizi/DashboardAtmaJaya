from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class Kategori_survey(models.Model):
    _name="dashboard_web.kategori_survey"
    _rec_name ="nama"

    jenis_survey = fields.Many2one('dashboard_web.jenis_survey',string="Jenis Survey",required=True)
    nama = fields.Char(string="Kategori", required=True)
    is_seleksi = fields.Selection([
        ('1', 'Yes'),
        ('0', 'No'),
    ], default='1', string="Seleksi dashboard", required=True)