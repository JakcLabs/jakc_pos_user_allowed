{
    'name': 'Jakc Labs - POS Users Allowed',
    'version': '10.0.0.1.0',
    'category': 'Point of Sale',
    'license': 'AGPL-3',
    'summary': 'Restricted User Only Access Certain POS',
    'author': "Jakc Labs",
    'website': 'http://www.jakc-labs.com/',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/ir_rule.xml',
        'views/res_users_view.xml',
    ],
    'installable': True,
    'application': True,
}
