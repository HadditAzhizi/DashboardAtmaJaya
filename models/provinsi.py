from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class Provinsi(models.Model):
    _name="dashboard_web.provinsi"
    _rec_name ="Nama_Provinsi"

    Id_map = fields.Char(string="Id Map")
    Nama_Provinsi = fields.Char(string='Nama Provinsi', required=True)#copy=False, readonly=True,index=True, default=lambda self: _('New')
