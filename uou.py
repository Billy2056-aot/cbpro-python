from urllib.parse import quote
from django.utils.encoding import iri_to_uri
quote('Paris & Orléans')
iri_to_uri('/favorites/François/%s' % quote('Paris & Orléans'))