# Copyright 2022 <mj@ayudoo.bg>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    'name': 'Warehouse Forecast Quantity',

    'summary': """
        Configure wheather the virtual/forecast quantity includes the incoming.""",

    'description': """
        Configure wheather the virtual/forecast quantity includes the incoming.""",

    'author': 'Michael Jurke, Ayudoo Ltd',
    'website': 'ayudoo.bg',

    'category': 'Sales',
    'version': '0.1',

    'depends': [
        'base',
        'stock',
    ],

    'data': [
        'views/stock_warehouse_view.xml',
    ],
    'license': 'LGPL-3',
}
