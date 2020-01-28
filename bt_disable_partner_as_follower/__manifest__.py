##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-BroadTech IT Solutions
#   (<http://www.broadtech-innovations.com/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Disable Partner as Follower',
    'version': '11.0.0.0.1',
    'category': 'Discuss',
    'summary': 'Prevent adding partners/customers as followers',
    'license': 'AGPL-3',
    'author': 'BroadTech IT Solutions Pvt Ltd, jeo Software',
    'website': 'http://www.jeosoft.com.ar/',
    'depends': [
        'mail',
        'sale'
    ],
    'data': [
    ],
    'demo': [
    ],
    'images': [
        'static/description/banner.jpg'
    ],
    'installable': True,
    'application': False,
}
