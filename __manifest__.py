{
    'name': 'SAI - Ruta Programada en Ventas',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        "security/ir.model.access.csv",
        'data/data_route_programmed.xml', 
        'views/sale_order_view.xml',
        'views/route_programmed_view.xml',
    ],
    'installable': True,
}
