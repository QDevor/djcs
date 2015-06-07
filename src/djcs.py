#*- coding: utf-8 -*- 
"""
Copyright (C) 2015 __QDevor__.
http://www.gnu.org/licenses/gpl-3.0.html
"""

import os
import sys

import subprocess

import misc
import core.collectingData as ccd

from quantdigger.kernel.datasource.data import set_dir
my_data_src=os.path.join(os.environ.get("QDKe_PYSP_PATH"), 'QuantDigger-0.141-py2.7.egg/quantdigger/kernel', 'datasource', 'data')
set_dir(my_data_src)
import third_party.quantdigger.quantdigger.demo.main as demo_main
import third_party.quantdigger.quantdigger.demo.mplot_demo as demo_mplot_demo
  
def collectingCS(code='000878'):
    ccd.xls(code)
    #ccd.db(code)

if __name__=='__main__':
	print misc.getVersionInfor()
	
	#collectingCS('600673')
	
	demo_main
