from odoo import models, fields

class Tratamiento(models.Model):
    _name = 'hospital.tratamiento'
    _description = 'Tratamiento'

    name = fields.Char(string='Nombre del Tratamiento', required=True)
    codigo = fields.Char(string='Código', required=True)
