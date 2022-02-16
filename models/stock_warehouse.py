from odoo import fields, models


class Warehouse(models.Model):
    _inherit = "stock.warehouse"
    _name = "stock.warehouse"

    include_incoming_qty = fields.Boolean(
        "Include Incoming Quantity",
        help="Specify if the forecast/virtual quantity includes the incoming.",
        default=True,
    )
