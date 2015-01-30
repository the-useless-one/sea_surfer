#!/usr/bin/env python3

def generate_html(url, data):
    html = '<html>\n\t<body>\n'

    html += '\t\t<form id="csrf_form" action="{0}" method="POST">\n'.format(url)

    for key, value in data.items():
        html += '\t\t\t<input type="hidden" name="{0}" value="{1}"/>\n'.format(key, value)

    html += '\t\t</form>\n'
    html += '\t\t<script>\n\t\t\tdocument.forms["csrf_form"].submit()\n\t\t</script>\n'
    html += '\t</body>\n</html>'

    return html

