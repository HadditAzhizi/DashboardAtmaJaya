from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from datetime import datetime,date


class survey(models.Model):
    _name="dashboard_web.survey"
    _rec_name ="survey"

    survey = fields.Many2one('dashboard_web.jenis_survey',string="Jenis Survey",required=True)
    isi_survey = fields.One2many('dashboard_web.isi_survey','survey', string='Survey')


 #    class ParentModel(models.Model):
	# _name = 'parent.model'

 #       template_id = fields.Many2one('product.template',string='Template')
 #       product_ids = fields.One2many(comodel_name = 'child.model', inverse_name = 'parent_id', string = 'Children Ids')

	# class ChildModel(models.Model):
	#      _name= 'child.model'
	 
	#      parent_id = fields.Many2one(comodel_name='parent.model', string="Parent")
	#      product_id = fields.Many2one(comodel_name='product.product', string="Product")
	#      lst_price = fields.Float("Sale Price")

	#      @api.onchange('product_id')
	#      def onchange_product_id(self):
	#         variant_ids_list = []
	#         if self._context.get('template_id'):   //  We will pass this context from the xml view.
	#             template_id = self.env["product.template"].browse(self._context.get('template_id'))
	#             for variant_id in template_id.product_variant_ids:
	#                 if variant_id.lst_price >  100:
	#                      variant_ids_list.append(variant_id.id)
	#         return result['domain'] = {'product_id': [('id','in',variant_ids_list)]