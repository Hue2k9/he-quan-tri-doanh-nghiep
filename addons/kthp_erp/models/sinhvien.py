from odoo import models, fields, api


class SinhVien(models.Model):
    _name = 'huehm'
    _description = 'Hoàng Minh Huệ - 2020607477'

    name = fields.Char(string="Họ và tên", required=True)
    code = fields.Char(string="Mã sinh viên", required=True)
    address = fields.Char(string="Địa chỉ")
    group = fields.Selection([
        ('group1', 'Nhóm 1'),
        ('group2', 'Nhóm 2'),
        ('group3', 'Nhóm 3')
    ], string='Nhóm')