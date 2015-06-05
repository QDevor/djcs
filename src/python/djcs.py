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

def collectingCS(code='000878'):
    #ccd.xls(code)
    ccd.db(code)

if __name__=='__main__':
	print misc.getVersionInfor()
	
	collectingCS('600673')
