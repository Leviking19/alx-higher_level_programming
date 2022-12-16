#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
use the package urllib
 body of the response must be displayed in tabulation before -
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("- Body:")
    print(body)

