# -*- coding: utf-8 -*-
import logging
import re
import calendar
from datetime import timedelta, date, datetime
from dateutil.relativedelta import relativedelta
import dateutil
import requests

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MailMessage(models.Model):
    _inherit = 'mail.message'
    odoo12_id = fields.Integer("odoo12_id", default=0)

    @api.model_create_multi
    def create(self, vals):
        events = super(MailMessage, self).create(vals)
        return events


class ApiMessageLog(models.Model):
    _name = 'api.message.log'
    _description = 'Api Message Log'

    name = fields.Char("Name")
    odoo12_id = fields.Integer("odoo12_id", default=10)
    subject = fields.Char('Subject')
    date = fields.Datetime('Date', default=fields.Datetime.now)
    body = fields.Html('Contents', default='')
    res_model = fields.Char('Related Document Model', index=True)
    res_model_name = fields.Char('Res model name', index=True)
    res_id = fields.Integer('Related Document ID', index=True)
    record_name = fields.Char('Message Record Name', help="Name get of the related document.")
    res_name = fields.Char('Res name')
    type = fields.Char('Type')
    datas = fields.Text('Datas')
    message_id = fields.Integer("Message Id")
    message_type = fields.Char('Message Type')
    subtype_id = fields.Char('Subtype Id')
    email_from = fields.Char('Email From', )
    reply_to = fields.Char('Reply To')
    message_action = fields.Char('Message Action')
    author_id = fields.Char('Author Id')
    rating_value = fields.Float('Rating Value')
    description = fields.Html('Description')
    display_name = fields.Char('Display name')

    datas_fname = fields.Char('datas_fname')
    mimetype = fields.Char('mimetype')
    index_content = fields.Char('index_content')
    datas = fields.Text('datas')
    is_message_attachment = fields.Boolean('is_message_attachment')

    message15_id = fields.Many2many('mail.message', string='Rec Message', )
    api_type = fields.Selection([('message', 'Message'),
                                 ('attachment', 'Attachment'),
                                 ], string='Api Type', default='message')
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel')
                              ], string='State', default='draft')

    a = [{"odoo12_id": 60502,
          "subject": "DUONG, Giang Nam on Legal Leaves 2021 : 0.38 day(s): Leaves Approval assigned to you",
          "date": "2021-12-31 09:33:21",
          "body": "<div style=\"margin:0px; padding:0px; font-size:13px\">\n    <span>Giang Nam Duong</span> assigned you an activity <span>Leaves Approval</span>\n    \n    on <span>DUONG, Giang Nam on Legal Leaves 2021 : 0.38 day(s)</span>\n    to close for <span>31-Dec-2021</span>.<br>\n    <p style=\"margin:16px 0px 16px 0px\">\n        <a style=\"background-color:#875A7B; padding:8px 16px 8px 16px; text-decoration:none; color:#fff; border-radius:5px\" href=\"/mail/view?model=hr.leave&amp;res_id=441\">\n            View Leave\n        </a>\n    </p>\n    <div style=\"margin-top:8px\"><p>New Legal Leaves 2021 Request created by Giang Nam Duong from 2021-12-31 09:00:00+07:00 to 2021-12-31 12:00:00+07:00</p></div>\n</div>\n        ",
          "model": False, "res_id": 0, "record_name": "DUONG, Giang Nam on Legal Leaves 2021 : 0.38 day(s)",
          "message_type": "notification", "subtype_id": "Note",
          "email_from": "\"Giang Nam Duong\" <namduong@hexience.com>",
          "reply_to": "\"Hexience Systems Limited\" <catchall@hexience.net>", "message_action": "message_edit_log",
          "author_id": "Giang Nam Duong", "rating_value": 0.0,
          "description": "DUONG, Giang Nam on Legal Leaves 2021 : 0.38 day(s): Leaves Approval assigned to you",
          "display_name": "DUONG, Giang Nam on Legal Leaves 2021 : 0.38 day(s)"}]

    def button_process_message(self):
        # get attachment
        url = "https://hexodoo12.dev.arestos.com/message/moving"
        payload = {}
        files = {}
        params = {'secret_key': '%0w)VujJ(DHUIj79vz#a',
                  'limit': 5}
        headers = {}
        response = requests.request("POST", url, headers=headers, params=params, data=payload, files=files)
        datas = response.json()
        for data in datas:
            data_create = {
                'api_type': 'message',
                'odoo12_id': data.get('odoo12_id', False),
                'subject': data.get('subject', ''),
                'name': data.get('name', ''),
                'date': data.get('date', ''),
                'datas_fname': data.get('datas_fname', ''),
                'description': data.get('description', ''),
                'res_name': data.get('res_name', ''),
                'res_model': data.get('res_model', '') or data.get('model', '') or '',
                'res_model_name': data.get('res_model_name', ''),
                'res_id': data.get('res_id', False),
                'type': data.get('type', ''),
                'message_type': data.get('message_type', 'comment'),
                'subtype_id': data.get('subtype_id', ''),
                'datas': data.get('datas', ''),
                'message_id': data.get('message_id', False),
                'display_name': data.get('display_name', ''),
                'mimetype': data.get('mimetype', ''),
                'index_content': data.get('index_content', ''),
                'is_message_attachment': data.get('is_message_attachment', False),

                'body': data.get('body', ''),
                'email_from': data.get('email_from', '"Administrator" <admin@example.com>')

            }
            self.create([data_create])
        a = [{"key": "secret_key", "value": "%0w)VujJ(DHUIj79vz#a", "description": ""},
             {"key": "res_id", "value": "20", "description": ""},
             {"key": "res_model", "value": "mail.message", "description": ""},
             {"key": "is_moving", "value": "False", "description": ""}]
        return True

    def button_process_attachment(self):
        # get attachment
        url = "https://hexodoo12.dev.arestos.com/attachment/moving"
        payload = {}
        files = {}
        params = {'secret_key': '%0w)VujJ(DHUIj79vz#a',
                  'limit': 5}
        headers = {}
        response = requests.request("POST", url, headers=headers, params=params, data=payload, files=files)
        datas = response.json()
        for data in datas:
            data_create = {
                'api_type': 'attachment',
                'odoo12_id': data.get('odoo12_id', False),
                'name': data.get('name', ''),
                'datas_fname': data.get('datas_fname', ''),
                'description': data.get('description', ''),
                'res_name': data.get('res_name', ''),
                'res_model': data.get('res_model', ''),
                'res_model_name': data.get('res_model_name', ''),
                'res_id': data.get('res_id', False),
                'type': data.get('type', ''),
                'datas': data.get('datas', ''),
                'message_id': data.get('message_id', False),
                'display_name': data.get('display_name', ''),
                'mimetype': data.get('mimetype', ''),
                'index_content': data.get('index_content', ''),
                'is_message_attachment': data.get('is_message_attachment', False),
                'message_type': data.get('message_type', 'comment'),
                'body': data.get('body', ''),
                'email_from': data.get('email_from', '"Administrator" <admin@example.com>')

            }
            self.create([data_create])
        a = [{"key": "secret_key", "value": "%0w)VujJ(DHUIj79vz#a", "description": ""},
             {"key": "res_id", "value": "20", "description": ""},
             {"key": "res_model", "value": "mail.message", "description": ""},
             {"key": "is_moving", "value": "False", "description": ""}]
        return True

    def button_create_data(self):
        message_obj = self.env['mail.message'].sudo()
        attachment_obj = self.env['ir.attachment']
        for rec in self:
            if rec.res_model:
                message_val = {
                    'odoo12_id': rec.odoo12_id,
                    'model': rec.res_model,
                    'res_id': rec.res_id,
                    'record_name': rec.name or '_',
                    'message_type': rec.message_type or 'comment',
                    'body': rec.body or '_',
                    'email_from': rec.email_from or '"Administrator" <admin@example.com>',
                    'author_id': 1,
                    'author_guest_id': False,
                }
                message15_id = message_obj.create([message_val])
                if message15_id:
                    rec.write({'message15_id': message15_id,
                               'state': 'done',
                               })
                    if rec.is_message_attachment:
                        attachment_id = attachment_obj.create({
                            'name': rec.name or 'name',
                            'type': rec.type or 'binary',
                            'datas': rec.datas or '',
                            'mimetype': rec.mimetype or 'image/png',
                            'res_model': rec.res_model or '',
                            'res_id': rec.res_id or 0,
                            'res_name': rec.res_name or '',
                        })
                        message15_id.write({
                            'attachment_ids': [(4, attachment_id.id)],
                        })

            return True
