from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Building(models.Model):
    _name = 'building'
    _description ='Building'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    no = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)

