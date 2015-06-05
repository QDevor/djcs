"""
Copyright (C) 2015 __QDevor__.
http://www.gnu.org/licenses/gpl-3.0.html
"""
from os.path import dirname as dirname
from os.path import join as pathjoin

import sys
mswindows = (sys.platform == "win32")

def getPath(sufix=""):
    '''get absolute path of the current dir'''
    path = dirname(__file__)
    try:
        index=path.index("..")
        if index!=-1:
            path=path[:index]
    except:
        pass
    if mswindows:
    	return pathjoin(path, sufix).replace('/','\\')
    else:
    	return pathjoin(path, sufix).replace('\\','/')

def getTopDir():
	path=getPath()
	path = dirname(path)
	path = dirname(path)
	return path

def getDir(sufix=""):
	if sufix == "":
		path = getTopDir()
	else:
		path = pathjoin(getTopDir(), sufix)
	
	if not os.path.exists(path):
	  os.makedirs(path)
	  
	return path

import subprocess
import commands

def getVersionInfor():
	path=getPath()
	cmd='''cd %s && git tag |sort -r |head -1''' % path
	version=subprocess.check_output(cmd, shell=True).strip('\n')
	if version.strip()=='':
		version='v1.0' 
	cmd='''cd %s && git log -1 |grep  commit |grep -o "\<[a-f0-9]\+\>"''' % path
	build=subprocess.check_output(cmd, shell=True).strip('\n')
	return (version, build)

import os

def __misc_init__():
  os.environ["DJCS_TOP_DIR"] = getDir()
  os.environ["QUANT_DIR"] = getDir("config")
  print 'DJCS_TOP_DIR = ' + os.environ.get("DJCS_TOP_DIR")
  print 'QUANT_DIR = ' + os.environ.get("QUANT_DIR")

__misc_init__()