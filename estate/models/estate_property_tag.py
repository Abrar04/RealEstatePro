from odoo import fields, models


class EstateProperties(models.Model):
    _name = "estate.property.tag"
    _description = "Tag Model for Real-Estate Properties"

    name = fields.Char(required=True, string="Properties Tag")

    _sql_constraints = [
        ('tag_name', 'UNIQUE(name)', 'Tag name must be unique.'),

    ]

