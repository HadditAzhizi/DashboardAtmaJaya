from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class Jenis_survey(models.Model):
    _name="dashboard_web.jenis_survey"
    _rec_name ="nama"

    nama = fields.Char(string="Jenis survey", required=True)
    is_publish = fields.Selection([
        ('1', 'Yes'),
        ('0', 'No'),
    ], default='1', string="Tampilkan di Dashboard", required=True)
    template = fields.Char(string="Template", required=True)
    kategori = fields.One2many('dashboard_web.kategori_survey','jenis_survey', string='Kategori')