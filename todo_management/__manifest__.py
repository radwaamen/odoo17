{
    'name': 'Todo Management',
    'version': '17.0.0.1.0',
    'category': '',
    'author': 'Radwa Mohammed',
    'depends': ['base', 'mail'],  # List of module dependencies
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/todo_task_view.xml'
    ],
    'application': True,  # Whether the module is an application (front-end)
}
