# -*- coding: utf-8 -*-
{
    'name': "GDOMEX",

    'summary': """ Módulo de GDOMEX """,

    'description': """
         Módulo para GDOMEX
    """,

    'author': "",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['stock','project', 'sale','mrp', 'stock_landed_costs'],

    'data': [
    	'report/venta_cotizacion_grupodomex.xml',
    	'report/instalacion_cotizacion_grupodomex.xml',
        'data/report_paperformat_data.xml',
        'report/report_oc_importaciones_almex.xml',
        'report/report_oc_importaciones_aplytek.xml',
        'report/report_orden_trabajo.xml',
        'report/report_purchase_orders.xml',
        'report/reporte_voucher_domex_bac.xml',
        'report/reporte_voucher_domex_bi.xml',
        'views/stock_quant_views.xml',
        'security/groups.xml',
        'views/stock_production_lot_views.xml',
        'views/contrasenia_pago.xml',
        'views/account_report.xml',
        'report/reporte_cheque_axir_g_t.xml',
        'report/reporte_voucher_aplytek.xml',
        'report/reporte_inter_continuo.xml',
        'security/ir.model.access.csv',
        'views/account_payments_views.xml',
        'views/project_project_views.xml',
        'views/stock_picking_views.xml',
        'views/sale_views.xml',
        'views/product_views.xml',
        'views/account_analytic_view.xml',
        'views/purchase_orders.xml',
        'views/report.xml',
        'views/report_saleordershipping_domex.xml',
        'views/report_so_almex.xml',
        'views/report_so_domex.xml',
        'views/report_so_aplytek.xml',
        'views/purchase_views.xml',
        'report/report_envio_domex.xml',
        'report/report_envio_aplytek.xml',
        'report/report_stockpicking_domex.xml',
        'report/report_envio_almex.xml',
        'report/report_orden_trabajo.xml',
        'views/mrp_production_views.xml',
        'wizard/project_orden_trabajo.xml',
        'views/stock_landed_cost_views.xml',
    ],
}
