{
    'name': 'App One',
    'version': '17.0.0.1.0',
    'category': '',
    'author': 'Radwa Mohammed',
    'depends': ['base',
                'sale_management'],  # List of module dependencies
    'data': [
        'views/base_menu.xml',
        'views/property_view.xml',
        'security/ir.model.access.csv',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/building_view.xml'
    ],
    'assets': {
        'web.assets_backend': ['app_one/static/src/css/property.css']
    },
    'application': True,  # Whether the module is an application (front-end)
}
