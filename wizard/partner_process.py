# -*- coding: utf-8 -*-

import time

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class PartnerProcess(models.TransientModel):
    _name = "res.partner.process"
    _description = "Procesar"

    @api.model
    def _count(self):
        return len(self._context.get('active_ids', []))
    count = fields.Integer(default=_count, string='# of Rutas')