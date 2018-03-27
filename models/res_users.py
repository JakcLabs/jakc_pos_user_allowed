from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError, Warning


class ResUser(models.Model):
    _inherit = 'res.users'

    pos_config_id = fields.Many2one('pos.config','Point of Sale')