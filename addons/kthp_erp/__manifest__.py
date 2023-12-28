# -*- coding: utf-8 -*-
{
    'name': "kthp_erp",

    'summary': """
        Thi kết thúc học phần""",

    'description': """
        Hệ quản trị doanh nghiệp điện tử - IT6061
    """,

    'author': "Hoàng Minh Huệ - 2020607477",
    'website': "https://www.haui.edu.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hệ thống thông tin',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sinhvien_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/sinhvien_demo.xml',
    ],
}
