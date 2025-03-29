from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    route_programmed_id = fields.Many2one(
        'sai.route.programmed',
        string='Ruta Programada',
        help='Ruta logística asignada para la recolección de residuos.'
    )
