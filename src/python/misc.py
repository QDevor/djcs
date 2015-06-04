"""
Copyright (C) 2015 __QDevor__.
http://www.gnu.org/licenses/gpl-3.0.html
"""
from os.path import dirname as dirname
from os.path import join as pathjoin

def getPath(sufix=""):
    '''get absolute path of the current dir'''
    path = dirname(__file__)
    try:
        index=path.index("..")
        if index!=-1:
            path=path[:index]
    except:
        pass
    return pathjoin(path, sufix).replace('\\','/')


import subprocess

def getVersionInfor():
    path=getPath()
    cmd="cd %s && git tag |sort -r |head -1" % path
    version=subprocess.check_output(cmd, shell=True).strip('\n')
    cmd='''cd %s && git log -1 |grep  commit |grep -o "\<[a-f0-9]\+\>"''' % path
    build=subprocess.check_output(cmd, shell=True).strip('\n')
    return (version, build)
