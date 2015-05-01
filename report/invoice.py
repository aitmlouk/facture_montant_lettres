# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution

#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2015  Ait-Mlouk Addi  ( aitmlouk@gmail.com)
#                        http://odoo-services.esy.es/

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from openerp import pooler
import time
from openerp.report import report_sxw
import convertion


class account_invoice_letters(report_sxw.rml_parse):

    def __init__(self, cursor, user, name, context):
        super(account_invoice_letters, self).__init__(cursor, user, name, context)
        self.localcontext.update({
            'time': time,
            'account_invoice':self.account_invoice,
            'sale_order':self.sale_order,
        })

    def account_invoice(self,ids):
        invoices=pooler.get_pool(self.cr.dbname).get('account.invoice').browse(self.cr,self.uid,[ids])
        for invoice in invoices:
            devis = invoice.currency_id.name
            montant = invoice.amount_total  
            return convertion.trad(montant, devis).upper()
        
    def sale_order(self,ids):
        invoices=pooler.get_pool(self.cr.dbname).get('sale.order').browse(self.cr,self.uid,[ids])
        for invoice in invoices:
            devis = invoice.currency_id.name 
            montant = invoice.amount_total  
            return convertion.trad(montant, devis).upper()

report_sxw.report_sxw('report.account.invoice.letters', 'account.invoice',
        'addons/facture_montant_lettres/report/invoice.rml',
        parser=account_invoice_letters)

report_sxw.report_sxw('report.sale.order.letters', 'sale.order',
        'addons/facture_montant_lettres/report/sale_order.rml',
        parser=account_invoice_letters)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

