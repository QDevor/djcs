"""
Copyright (C) 2015 __QDevor__.
http://www.gnu.org/licenses/gpl-3.0.html
"""
import os
import sys
from os.path import join as pathjoin

mswindows = (sys.platform == "win32")

def __misc_init__():
  DJCS_TOP_DIR = os.environ.get('DJCS_TOP_DIR')
  DJCS_CORE_DIR = pathjoin(DJCS_TOP_DIR, 'src/core/').replace('/','\\').strip('\\')
  print 'DJCS_CORE_DIR = ' + DJCS_CORE_DIR

__misc_init__()