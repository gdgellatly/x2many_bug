# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class SubSaleOrderLine(models.Model):

    _name = 'sub.sale.order.line'
    _description = 'Sub Sale Order Line'

    name = fields.Char()
    product_id = fields.Many2one(comodel_name='product.product')
    sale_line_id = fields.Many2one(comodel_name='sale.order.line')
    non_conflicting_field_name = fields.Char()

    @api.model
    def create(self, vals):
        print('Sub Line Create')
        print(vals)
        return super(SubSaleOrderLine, self).create(vals)

    @api.multi
    def write(self, vals):
        print('Sub Line Write')
        print(vals)
        return super(SubSaleOrderLine, self).write(vals)


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    sub_order_line_ids = fields.One2many(
        comodel_name='sub.sale.order.line',
        inverse_name='sale_line_id',
    )

    @api.multi
    def write(self, vals):
        print('Order Line Write')
        print(vals)
        return super(SaleOrderLine, self).write(vals)

    @api.model
    def create(self, vals):
        print('Order Line Create')
        print(vals)
        return super(SaleOrderLine, self).create(vals)


class Sale(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def write(self, vals):
        print('Order Write')
        print(vals)
        return super(Sale, self).write(vals)

    @api.model
    def create(self, vals):
        print('Order Create')
        print(vals)
        return super(Sale, self).create(vals)
