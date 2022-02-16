from odoo import models
from odoo.tools.float_utils import float_round


class Product(models.Model):
    _inherit = "product.product"

    def _compute_quantities_dict(self, *args, **kwargs):
        self = self.sudo()
        res = super()._compute_quantities_dict(*args, **kwargs)

        if not res:
            return res

        warehouse = None
        warehouse_id = self.env.context.get("warehouse")
        if warehouse_id:
            warehouse = self.env["stock.warehouse"].browse(warehouse_id)
        else:
            website_id = self.env.context.get("website_id")
            if website_id:
                website = self.env["website"].browse(website_id)
                warehouse = website.warehouse_id

        if warehouse:
            if not warehouse.include_incoming_qty:
                for product_id, data in res.items():
                    product = self.env["product.product"].browse(product_id)
                    data["virtual_available"] = float_round(
                        data["qty_available"] - data["outgoing_qty"],
                        precision_rounding=product.uom_id.rounding,
                    )

        return res
