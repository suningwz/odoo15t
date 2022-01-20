# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResArea(models.Model):
    _name = 'res.area'
    _description = 'Area'

    name = fields.Char('Name', required=True, )
    code = fields.Char('Code')
    manager_id = fields.Many2one('res.users', string='Manager')
    user_ids = fields.Many2many('res.users', 'res_area_user_rel', string='Users')
