from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description ='Property'

    name = fields.Char(required=1)
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_avialability= fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff')
    living_area = fields.Integer()
    bedrooms = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')


    state = fields. Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed')
    ], default='draft')


    _sql_constraints = [('unique_name', 'unique("name")', 'this name is exist')]
    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms== 0:
                raise ValidationError('please add valid number of bedrooms!')
    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        print("inside create method")
        return res

    @api.model
    def search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
        print("inside search method")
        return res

    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    def write(self, vals):
        res = super(Property, self).write(vals)
        print("inside write method")
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        print("inside unlink method")
        return res


    def action_draft(self):
        for rec in self:
         print("inside draft action")
         rec.state = 'draft'

    def action_pending(self):
         for rec in self:
            print("inside pending action")
            rec.state = 'pending'

    def action_sold(self):
         for rec in self:
            print("inside sold action")
            rec.state = 'sold'

    def action_colsed(self):
        for rec in self:
            rec.state = 'closed'


    @api.model
    def create(self, vals):
        record = super(Property, self).create(vals)
        record.message_post(body="This is an automatic message to the chatter.")


