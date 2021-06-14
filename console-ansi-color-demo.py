# @echo off
# rem='''
# set pythonioencoding=utf8
# python -i -x "%~f0" %*
# exit /b 
# '''

from os import system as s;s('');any( print(*(f'\33[7;{z}{y}m{z+y:>4}' for y in map(str,range(30,38))),end=' \33[m\n') for z in ('','1;') )