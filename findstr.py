# @echo off
# rem='''
# set pythonioencoding=utf8
# python -i -x "%~f0" %*
# exit /b 
# '''



import fileinput as fi
from sys import argv as a
from pathlib import Path as p
from os import system as sys
from re import search
sys('')
def r(i=None,e='utf8'):
    with fi.FileInput(files=i,openhook=fi.hook_encoded(e, 'backslashreplace')) as f:
        yield from ((x.rstrip('\n'),f) for x in f)

h = lambda z:(j for x in z for j in x)


m = lambda x=0:f'\33[{x}m'

s = lambda x:repr(x)[1:-1]if search(r'[\x00-\x08\x0b-\x1f]',x) else x 
sp = lambda k,x:h((x[:a],x[a:b],x[b:]) for a,b in (search(k,x).span(),))
tpl = ('',m('7;37'),m(0))
w = lambda x,k:''.join(h(zip(tpl,map(s,sp(k,x)))))
lr = il = lambda k,x: k in x
ir = lambda k,x: search(k,x)
f = lambda i,k:((y.filename(),y.filelineno(),w(x.strip(),k)) for x,y in i if lr(k,x))

pre = [*map(m,('7;32','7;36',0))]
c = lambda z:zip(pre,z)

e = m(0)+'\n'

k,i=a[1:2]and a[1]or 'pyd',a[2:3]and a[2]or '*.7z'
lr = ir if k[0]==k[-1]=='\'' else il 
k = k[1:-1] if lr==ir else k
any(print(*h(c(x)),end=e) for y in p().glob(i) if y.is_file() for x in f(r([y]),k))



