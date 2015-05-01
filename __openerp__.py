# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution

#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2014  Ait Mlouk Addi (http://odoo-services.esy.es/)   Gmail : aitmlouk@gmail.com.

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
{
    'name': 'Commande/Facture montant en lettres FR',
    'version': '1.0',
    'depends': ['account'],
    "author" : "Ait-Mlouk Addi",
    "website" : "http://aitmlouk.esy.es/",
    'description': 'Module qui permet de  convertir le montant d/une commmande / facture au lettres (en Francais) et l"ajoute  au rapport de la facture',
    'category': 'Generic Modules/Accounting',
    'icon': '/facture_montant_lettres/static/src/img/icon.png',
    'update_xml': ['report.xml'],

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

