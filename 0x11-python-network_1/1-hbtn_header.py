#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""

import sys
from urllib.request import urlopen

# Get the URL from the command line argument
url = sys.argv[1]

# Send a request to the URL and get the response
with urlopen(url) as response:
    # Get the headers from the response
    headers = response.info()

    # Get the value of the X-Request-Id header
    request_id = headers.get("X-Request-Id")

    # Print the value of the X-Request-Id header
    print(request_id)
