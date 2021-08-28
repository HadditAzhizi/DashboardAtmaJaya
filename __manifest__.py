# -*- coding: utf-8 -*-
{
    'name': "dashboard_web",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','web','bus'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/sumber_air.xml',
        'views/bb_utama.xml',
        'views/bb_cadangan.xml',
        'views/pemilahan_sampah.xml',
        'views/perlakuan_sb3.xml',
        'views/perlakuan_uts.xml',
        'views/sumber_pu.xml',
        'views/prov.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
