# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2011 Pexego (<www.pexego.es>). All Rights Reserved
#    $Omar Castiñeira Saavedra$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

"""Adds the functionally of block prodlots by food alerts"""

# pylint: disable-msg=C0103

import block_prodlots_plpgsql_functions
import res_groups
import stock_location
import block_prodlot_case
import stock_production_lot
import product
import stock_move
import report_partners_affected_bycase
import stock_picking
import partner
import wizard

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
