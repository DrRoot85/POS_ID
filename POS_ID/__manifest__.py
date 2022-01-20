# -*- coding: utf-8 -*-

{
    'name': "POS - National ID/ IQama Customer",

    'summary': """
        Add National ID/ IQama type field to pos customer view.
    """,

    'description': """
        Add National ID/ IQama type field to pos customer view.
    """,

    'author': "Dr.Root",
    'website': "---Not Yet ----",

    'category': 'Sales/Point of Sale',
    'version': '0.1',
    'price': 0.00,
    'currency': 'USD',

    'depends': ['point_of_sale','contacts','base'],

   'data': [
        'views/res_partner.xml',
        'views/res_company.xml',

    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_id/static/src/js/models.js',
            'pos_id/static/src/js/screens.js',
        ],
        'web.assets_qweb': [
            'pos_id/static/src/xml/**/*',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
