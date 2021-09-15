from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class Isi_survey(models.Model):
    _name="dashboard_web.isi_survey"

    provinsi = fields.Many2one('dashboard_web.provinsi',string="Provinsi",required=True)
    kategori = fields.Many2one('dashboard_web.kategori_survey',string="Kategori",required=True)
    persentase = fields.Float(string="Presentase",required=True)
    survey = fields.Many2one('dashboard_web.survey', string='Survey', store=True, readonly=False)