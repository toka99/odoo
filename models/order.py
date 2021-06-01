from odoo import models, fields, api

class Order(models.Model):
    _name = 'toka2.order'
    _description = 'Description'

    name = fields.Char()
    date = fields.Date()
    timestamp=fields.Datetime()
    model_2 = fields.One2many('toka2.basic.model2','order')
    partner = fields.Many2one('res.partner')
    
