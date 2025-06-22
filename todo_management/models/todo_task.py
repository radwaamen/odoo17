from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Task Name')
    description = fields.Text()
    due_date = fields.Date()
    assign_to_id = fields.Many2one('res.partner')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string="Status")

    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new', tracking=True)

    @api.model
    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'
