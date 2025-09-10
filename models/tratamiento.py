# Importa las clases necesarias de Odoo:
# - models: para crear modelos (tablas) en Odoo.
# - fields: para definir los tipos de campos (Char, Text, Integer, etc.)

from odoo import models, fields

class Tratamiento(models.Model):
    _name = 'hospital.tratamiento'
    _description = 'Tratamiento'

    name = fields.Char(string='Nombre del Tratamiento', required=True)
    codigo = fields.Char(string='Código', required=True)
