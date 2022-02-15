Warehouse Forecast Quantities
=============================

.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

Configure whether to include incoming quantity in forecast quantity, for example, in
your website stock. This is useful if you don't want to sell products whose incoming
deliveries are confirmed, but are not received.


**Table of contents**

.. contents::
   :local:


Usage
-----

In `Inventory` -> `Configuration` -> `Warehouses` open the warehouse in question. In the
`Product Forecast Quantities` input group uncheck ``include incoming``.


With and without incoming quantities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on your configuration, you may need to handle both cases: with and without
incoming quantity. For example, for your stock rules to work properly or for
manually created sales orders in the admin backend.

To achieve this, you configure multiple warehouses with different settings, where
the location of the warehouse without ``include incoming`` is a child of the root
warehouse.


Example configuration
^^^^^^^^^^^^^^^^^^^^^

* a warehouse `WebWH` with ``include incoming`` unchecked
* a `RootWH`
* you configure your website to use `WebWH` as warehouse. Users will see the stock
  without the quantities that yet have to be received and out-of-stock products cannot
  be ordered.
* you open the location for `WebWH` of location type ``view``, and change the
  `Parent Location` to `RootWH/Stock`
* add a putaway rule to `RootWH/Stock` that moves all products to `WebWH`.

Depending on the desired behavior in the admin backend, you can either choose `WebWH`
or `RootWH` as sales order warehouse.


Bug Tracker
-----------

Bugs are tracked on `GitHub Issues <https://github.com/ayudoo/warehouse_forecast_quantity>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ayudoo/warehouse_forecast_quantity/issues/new**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
-------

Authors
^^^^^^^

* Michael Jurke
