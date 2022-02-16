# Copyright 2022 <mj@ayudoo.bg>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "author": "Michael Jurke, Ayudoo Ltd",
    "name": "Warehouse Forecast Quantity",
    "version": "0.1",
    "summary": "Forecast quantity with/without incoming.",
    "description": """
        Configure wheather the virtual/forecast quantity includes the incoming.""",
    "license": "LGPL-3",
    "category": "Sales/Sales",
    "support": "support@ayudoo.bg",
    "depends": [
        "base",
        "stock",
    ],
    "data": [
        "views/stock_warehouse_view.xml",
    ],
}
