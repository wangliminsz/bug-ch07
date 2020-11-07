# -*- coding: utf-8 -*-
{
    'name': "bug管理",

    'summary': """
        用于软件开发过程当中bug的管理""",

    'description': """
        用于软件开发过程当中bug的管理
    """,

    'author': "Scott",
    'website': "http://www.scott-odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
        
        #'views/bugs_adv.xml',
        #'views/bugs_stage.xml',
        
        # ---- attention -----
        # bugs_adv.xml & bugs_stage.xml, code all combined in bugs.xml 
                    
        'views/follower.xml',
        'views/bugs_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
