## -*- coding: utf-8 -*-

from openerp import models, fields, api, _, tools
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
_logger = logging.getLogger(__name__)
class SaleOrder(models.Model):
    _inherit = "sale.order"
    reason_rejection = fields.Many2one('reason.rejection',string="Motivo de Rechazo")
    zona = fields.Char(string="Zona")

    @api.onchange('partner_id')
    def zonapartner(self):
        self.zona = self.partner_id.zona