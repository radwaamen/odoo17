""" Initialize Hr Payslip Worked Days """

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError, Warning


class HrPayslipWorkedDays(models.Model):
    """
        Inherit Hr Payslip Worked Days:
         - 
    """
    _inherit = 'hr.payslip.worked_days'
    
    actual_no_of_hours = fields.Float(
        readonly=1
    )