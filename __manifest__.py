# -*- coding: utf-8 -*-
{
    'name': "Salary Rules",

    'summary': """Salary Rules""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Babatope Ajepe",
    'website': "http://ajepe.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/hr.payroll.structure.csv',
        'data/hr.salary.rule.category.csv',
        'data/hr.contribution.register.csv',
        'data/hr.salary.rule.csv',
    ],
}