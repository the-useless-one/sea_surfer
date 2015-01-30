#!/usr/bin/env python3

from html_parser import parse_headers, parse_data

def split_page_headers_data(request):
    str_headers, str_data = request.split('\n\n')
    page, str_headers = str_headers.split('\n', 1)
    page = page.split(' ')[1]

    headers = parse_headers(str_headers)
    data = parse_data(str_data)

    return page, headers, data

