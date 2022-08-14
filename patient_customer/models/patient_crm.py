from odoo import fields,models
from odoo.exceptions import UserError
class CRMPatientInherit(models.Model):
    _inherit = "res.partner"
    related_patient_id=fields.Many2one('hospital.patient')
    def unlink(self):
        if not self.related_patient_id:
            super().unlink()
        else:
            raise UserError("You Cant delete Customers related with patient")

