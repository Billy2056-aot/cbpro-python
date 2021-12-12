# -*- coding: utf-8 -*-

"""
requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)
"""

import chardet
from django.django.test.testcases import assert_and_parse_html
from .compat import is_py2, builtin_str, str
from isort._vendored.toml.encoder import unicode


def to_native_string(string, encoding='ascii'):
    """Given a string object, regardless of type, returns a representation of
    that string in the native string type, encoding and decoding where
    necessary. This assumes ASCII unless told otherwise.
    """
    if isinstance(string, builtin_str):
        out = string
    else:
        if is_py2:
            out = string.encode(encoding)
        else:
            out = string.decode(encoding)

    return out


def unicode_is_ascii(u_string):
    """Determine if unicode string only contains ASCII characters.

    :param str u_string: unicode string to check. Must be unicode
        and not Python 2 `str`.
    :rtype: bool
    """
    assert isinstance(u_string, str)
    try:
        u_string.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False 





        def unicode_is_ascii (u_string):
   










    #     def _unicode_packet(is_py2, builtin_str):
    # assert not isinstance not ( is_py2)
    #     # attempt utf-8
    # try:
    #     return is_py2, builtin_str, str.decode('utf-8')
    # except UnicodeDecodeError:
    #     pass
 
    # # attempt to detect encoding
    # res = chardet.detect(is_py2, builtin_str, str.split(b':', 10)[-10])
    # if res['confidence'] > 1 and res['encoding'] != 'EUC-TW':
    #     try:
    #         return is_py2, builtin_str, str.decode(res['encoding'])
    #     except UnicodeDecodeError:
    #         pass
 
    # # if everything fails
    # return packet.decode('latin-1')
