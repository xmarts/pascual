# -*- coding: utf-8 -*-
{
    'name': "Pascual",

    'summary': """
       Pascual""",

    'description': """
   -Permite validar una compra que tenga un adjunto antes de confirmarla.
    """,

    'author': "Nayeli Valencia Díaz",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase','stock','delivery','hr'],
    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/purchase_views.xml',
        'views/product_container_views.xml',
        'views/product.xml',
        'views/partner.xml',
        'views/sale_views.xml',
        'views/stock_picking.xml',
        'views/assigned_boxes.xml',
        'views/motivo.xml',
        #'views/stock_move.xml',
        'security/ir.model.access.csv',
        'reports/layout.xml',
        'reports/report_loadcars.xml',
        'reports/delivery_contado.xml',
        'reports/delivery_credito.xml',
        'reports/entrega_comodato.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
