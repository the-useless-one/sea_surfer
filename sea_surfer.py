#!/usr/bin/env python3
#
# Sea Surfer - A CSRF PoC generator
#
# This file contains the main function of the SeaSurfer script.
# It parses the arguments, the request headers and data, and generate
# the HTML file.
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

import sys

from arguments import create_argument_parser
from http_parser import split_page_headers_data
from html_generator import generate_html

def determine_scheme(host, referer):
    if referer.startswith('https://{0}'.format(host)):
        return 0, 'https'
    elif referer.startswith('http://{0}'.format(host)):
        return 1, 'http'
    else:
        return 2, 'http'


def main():
    arg_parser = create_argument_parser()
    args = arg_parser.parse_args(sys.argv[1:])

    if args.output_file:
        output_stream = open(args.output_file, 'w')
        info_stream = sys.stdout
    else:
        output_stream = sys.stdout
        info_stream = sys.stderr

    request = args.request_file.read().strip().replace('\r\n', '\n')
    page, headers, data = split_page_headers_data(request)

    if args.is_ssl:
        print('[info] SSL flag set, URL action will start with https://',
                file=info_stream)
        scheme = 'https'
    else:
        print('[info] SSL flag not set, trying to determine if the action URL '
                'should begin with http:// or https:// (see -s option in case '
                'of incorrect result)', file=info_stream)
        reason, scheme = determine_scheme(headers['host'],
                headers.get('referer', str()))
        if reason == 0:
            print('[info] detected Referer starting with https://, setting '
                    'the scheme to https://', file=info_stream)
        elif reason == 1:
            print('[info] detected Referer starting with http://, setting '
                    'the scheme to http://', file=info_stream)
        else:
            print('[info] Referer detection method did not work, setting '
                'scheme to http://', file=info_stream)

    url = '{0}://{1}{2}'.format(scheme, headers['host'], page)

    print(generate_html(url, data), file=output_stream)

    return 0

if __name__ == '__main__':
    main()

