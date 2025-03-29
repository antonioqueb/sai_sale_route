from odoo import models, fields

class RouteProgrammed(models.Model):
    _name = 'sai.route.programmed'
    _description = 'Ruta Programada de Recolección'

    name = fields.Char(string='Nombre de Ruta', required=True)
    description = fields.Text(string='Descripción')
    active = fields.Boolean(default=True)
