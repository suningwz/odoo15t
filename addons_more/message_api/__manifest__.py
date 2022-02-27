# -*- coding: utf-8 -*-


{
    "name": "Message Api",
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    "summary": "Message Api",
    'description': "Message Api",
    'category': 'base',
    'author': '',
    'company': '',
    'website': '',
    'depends': [
        'base', 'mail',
        'sale'
    ],
    'data': [

        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/api_message_log_view.xml',

    ],
    'images': [],

    'installable': True,
    'auto_install': False,
}
