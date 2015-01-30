#!/usr/bin/env python3
#
# Sea Surfer - A CSRF PoC generator
#
# This file contains the HTTP request parser.
# The first function splits the HTTP request in three parts : the page, the
# headers, and the POST data.
# The second function takes the headers and generate a Python dictionary.
# The third function takes the POST data, and generate a Python dictionary
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

from urllib.parse import parse_qs

def split_page_headers_data(request):
    str_headers, str_data = request.split('\n\n')
    page, str_headers = str_headers.split('\n', 1)
    page = page.split(' ')[1]

    headers = parse_headers(str_headers)
    data = parse_data(str_data)

    return page, headers, data

def parse_headers(str_headers):
    headers = dict()

    for str_header in str_headers.splitlines():
        header, value = str_header.split(':', 1)
        header = header.strip().lower()
        value = value.strip().lower()
        headers[header] = value

    return headers

def parse_data(str_data):
    data = dict()

    for key, value in parse_qs(str_data).items():
        data[key] = value[0]

    return data

