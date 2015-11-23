'''
python wrapper for JSON to HTML-Table convertor
(c) 2013 Varun Malhotra. MIT License
'''

import sys

if sys.version_info[0] == 2:
  from jsonconv import *
else:
  from jsonconv3 import *

__author__ = 'Varun Malhotra'
__version__ = '0.3'
__license__ = 'MIT'
