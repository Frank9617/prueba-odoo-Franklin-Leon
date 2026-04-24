{
    'name': 'IT Inventory Insumos',
    'version': '1.0',
    'summary': 'Control de insumos IT por sede',
    'description': 'Permite gestionar insumos de mantenimiento de equipos de computo',
    'author': 'Franklin Leon',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/insumo_views.xml',
    ],
    'installable': True,
    'application': True,
}