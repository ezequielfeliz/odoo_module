#json manifest
{
    'name': 'Vertical Hospital',
    'version': '1.0',
    'category': 'Hospital',
    'summary': 'Gestión de pacientes y tratamientos',
    'author': 'Smailyn Feliz',
    'website': 'https://asettech.com/',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu_views.xml',
        'views/paciente_views.xml',
        'views/tratamiento_views.xml',
    ],
    #logo que aparece en el modulo
    'images': ['static/description/icon.png'],
    'application': True,
}
