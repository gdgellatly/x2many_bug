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


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    sub_order_line_ids = fields.One2many(
        comodel_name='sub.sale.order.line',
        inverse_name='sale_line_id',
    )
