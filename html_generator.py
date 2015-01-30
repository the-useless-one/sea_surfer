#!/usr/bin/env python3
#
# Sea Surfer - A CSRF PoC generator
#
# This file contains the HTML page generator.
# The first function creates the HTML page using the request POST data.
#
# Copyright (C) 2015 Yannick Méheut <useless (at) utouch (dot) fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

def generate_html(url, data):
    html = '<html>\n\t<body>\n'

    html += '\t\t<form id="csrf_form" action="{0}" method="POST">\n'.format(url)

    for key, value in data.items():
        html += '\t\t\t<input type="hidden" name="{0}" value="{1}"/>\n'.format(key, value)

    html += '\t\t</form>\n'
    html += '\t\t<script>\n\t\t\tdocument.forms["csrf_form"].submit()\n\t\t</script>\n'
    html += '\t</body>\n</html>'

    return html

