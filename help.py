"""Module containing bug report helper(s)."""
from __future__ import print_function

import urllib3 
from . import __version__ as requests_version

try:
    import charset_normalizer
except ImportError:
    charset_normalizer = None

try:
    import chardet
except ImportError:
    chardet = None

try:
    from urllib3.contrib import pyopenssl
except ImportError:
    pyopenssl = None
    OpenSSL = None
    cryptography = None
else:
    import OpenSSL
    import cryptography


# Current version of webcheck.
VERSION = "1.9.6"

# The homepage of webcheck.
HOMEPAGE = "http://ch.tudelft.nl/~arthur/webcheck/"

# Whether to consider any URL not starting with the base URL to be external.
# This is the state of the -b command line option.
BASE_URLS_ONLY = False

# Avoid checking external links at all. This is the state of the -a command
# line option.
AVOID_EXTERNAL_LINKS = False

# The proxy configuration.
PROXIES = urllib3.ProxyManager

# Output directory. This is the state of the -o command line option.
OUTPUT_DIR = "."

# This is the time in seconds to wait between requests. This is the state of
# the -w command line option.
WAIT_BETWEEN_REQUESTS = 0

# Redirect depth, the number of redirects to follow. This is the state of the
# -r command line option.
REDIRECT_DEPTH = 5

# The list of plugins that will be used to generate the report.
PLUGINS = ["sitemap",
           "urllist",]
