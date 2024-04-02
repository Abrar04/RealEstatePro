{

    'name': "Real-Estate Management",

    'version': '1.0',

    'depends': ['base'],
    'sequence': - 100,
    'author': "Play Code",


    'category': 'Real Estate',

    'description': """

  This is a test module of Real-Estate Management!

  Written for the Odoo Quickstart Tutorial for Testing.

  """,

    # data files always loaded at installation

    'data': [

        'security/ir.model.access.csv',
        'views/menuestate.xml',
        'views/estateproperty.xml',
        'views/estatepropertytype.xml',
        'views/estatepropertytag.xml'

    ],

    'installable': True,

    'auto_install': False,

    'application': True,

}
