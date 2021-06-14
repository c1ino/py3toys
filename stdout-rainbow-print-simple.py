# @echo off
# rem='''
# set pythonioencoding=utf8
# rem python -i -x "%~f0" %*
# python -x "%~f0" %*
# exit /b 
# '''

import fileinput as fi
from os import system
from itertools import cycle
import argparse
from sys import stdout, stdin
import re


parser = argparse.ArgumentParser()

val = set(range(8)) - {0,4}
val = list(val)
val.sort()
from pprint import pprint as pp


system('')
line = []
sep = ' '
colors = cycle(val)
code = next(colors)
while 1:
    ch = stdin.read(1)
    if ch == '\n':
        _line = []
        for ch in re.split(r'(\s+)', ''.join(line)):
            if sep not in ch:
                _line.append(f'\033[3{code}m{ch}\033[0m')
                code = next(colors)
            else:
                _line.append(ch)
        print(''.join(_line), flush=True)
        line = []
        colors = cycle(val)
        code = next(colors)
        # stdout.flush()
        continue
    elif ch == '':
        break
    line.append(ch)
