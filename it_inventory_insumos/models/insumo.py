from odoo import models, fields

class ItInsumo(models.Model):
    _name = 'it.insumo'
    _description = 'Insumos IT'

    name = fields.Char(string='Nombre del Insumo', required=True)

    categoria = fields.Selection([
        ('toner', 'Tóner'),
        ('cable', 'Cable'),
        ('repuesto', 'Repuesto'),
        ('herramienta', 'Herramienta'),
        ('otro', 'Otro')
    ], string='Categoría')

    sede = fields.Selection([
        ('bogota', 'Bogotá Principal'),
        ('sede2', 'Sede 2'),
        ('san_martin', 'San Martin'),
        ('granada', 'Granada CILA')
    ], string='Sede')

    cantidad_stock = fields.Integer(string='Cantidad en Stock')
    cantidad_minima = fields.Integer(string='Cantidad mínima de alerta')
    precio_unitario = fields.Float(string='Precio Unitario')

    proveedor_id = fields.Many2one('res.partner', string='Proveedor')

    alerta_stock = fields.Boolean(string='Alerta', compute='_compute_alerta_stock')

    def _compute_alerta_stock(self):
        for record in self:
            record.alerta_stock = record.cantidad_stock < record.cantidad_minima