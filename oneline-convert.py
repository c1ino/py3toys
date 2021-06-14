# @echo off
# rem='''
# set pythonioencoding=utf8
# python -i -x "%~f0" %*
# exit /b 
# '''

import fileinput as fi

def i():
    print('<<<')
    with fi.input() as f:
        yield from f


trans = dict((c,f'\\x{c:x}') for c in map(ord,r'\'"^%!'))
def o(x):
    if not x.strip():
        return ''
    pre = ''
    while x.startswith(' '*4):
        x = x[4:]
        pre +='\\t'
    if x.startswith('#'):
        return ''

    x = x.rstrip('\n')
    x = x.translate(trans)


    return pre+x+r'\n'


def m():
    src, dst = [], []
    for x in i():
        src.append(x)
        dst.append(o(x))
    cmd = """python -c "exec('''{0}''')" """ 
    print(cmd.format(''.join(dst)))
    return src, dst

m()

