#!/usr/bin/env python3

from urllib.parse import parse_qs

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

