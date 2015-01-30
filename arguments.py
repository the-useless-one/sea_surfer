#!/usr/bin/env python3

import argparse

def create_argument_parser():
    arg_parser = argparse.ArgumentParser(prog='sea_surfer',
        description='A CSRF PoC generator')

    # The input file where the request is stored
    arg_parser.add_argument('-i',
        dest='request_file', type=argparse.FileType('r'),
        required=True, help='file containing the request')

    # A flag used to determine whether the action URL starts with HTTPS
    arg_parser.add_argument('-s', action='store_true', dest='is_ssl',
        help='if this flag is set, the form will have an HTTPS action URL')

    # The output file. If not specified, the result will be printed to stdout
    arg_parser.add_argument('-o', dest='output_file', type=str,
        help='HTML output file (default: stdout)')

    return arg_parser

