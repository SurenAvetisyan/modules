# -*- coding: utf-8 -*-
{
    'name': "freelance_habr",

    'summary': """Habr""",

    'description': """Habr""",

    'author': "Avetisyan",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'freelance_habr/static/src/css/style.css',
        ],
    },
}
