from odoo import models, fields, api

""" mail.thread: permite hacer seguimiento de cambios y enviar notificaciones.
- mail.activity.mixin: permite asignar actividades relacionadas al paciente."""

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre y Apellido', required=True, tracking=True)
    sequence = fields.Char(string='Código', required=True, copy=False, readonly=True,
                           default=lambda self: self.env['ir.sequence'].next_by_code('hospital.paciente'))
    rnc = fields.Char(string='RNC', tracking=True)
    tratamiento_id = fields.Many2one('hospital.tratamiento', string='Tratamiento', tracking=True)
    fecha_alta = fields.Datetime(string='Fecha de Alta', default=fields.Datetime.now)
    fecha_actualizacion = fields.Datetime(string='Fecha de Actualización', default=fields.Datetime.now)
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('alta', 'Alta'),
        ('baja', 'Baja')
    ], string='Estado', default='borrador', tracking=True)
    
    #validacion del RNC

    @api.onchange('rnc')
    def _check_rnc(self):
        if self.rnc and not self.rnc.isdigit():
            return {
                'warning': {
                    'title': "RNC inválido",
                    'message': "El RNC solo puede contener números.",
                }
            }
