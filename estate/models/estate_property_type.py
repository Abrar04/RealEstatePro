from odoo import fields, models


class EstateProperties(models.Model):
    _name = "estate.property.type"
    _description = "Types Model for Real-Estate Properties"

    name = fields.Char(required=True, string="Name")
    _sql_constraints = [
        ('property_name', 'UNIQUE(name)', 'Property Name must be unique.'),

    ]

