#!/usr/bin/env python3
#
# Sea Surfer - A CSRF PoC generator
#
# This file contains the argument parser.
# The first function creates an argument parser using the argparse library.
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

