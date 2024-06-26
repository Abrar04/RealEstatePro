from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'
    _description="User Model"

    property_ids = fields.One2many("estate.property", "user_id", string="Properties", domain=[("state", "in", ["new", "offer_received"])])