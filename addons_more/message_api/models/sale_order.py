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


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    odoo12_id = fields.Integer("odoo12_id", default=0)

    @api.model_create_multi
    def create(self, vals):
        events = super(SaleOrder, self).create(vals)
        return events

