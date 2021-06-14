from sys import _getframe as sys_getframe
from string import Formatter as string_Formatter


class debugFormatter(string_Formatter):
    def parse(self, format_string):
        _result = super().parse(format_string)
        return self.after_parse(_result)

    def after_parse(self, _result):
        for literal_text, field_name, *__ in _result:
            if field_name and '=' in field_name:
                _name, _rest = field_name.split('=', 1)

                # literal_text = f'{literal_text}{_name}='

                # optional: preserving whitespace around the equals sign
                _len, _rest = len(_rest), _rest.lstrip()
                _suffix = ' '*(_len-len(_rest))
                literal_text = f'{literal_text}{_name}={_suffix}'

                field_name = _name.rstrip() + _rest
            yield (literal_text, field_name, *__)


class evalFormatter(debugFormatter):
    '''src: https://mail.python.org/pipermail/python-ideas/2015-July/034695.html'''
    def __init__(self, globals, locals):
        self.globals = globals
        self.locals = locals

    def get_value(self, key, args, kwargs):
        key = str(key)
        return eval(key, self.globals, self.locals)


# default to looking at the parent's frame
def fstr(_str, level=1):
    '''src: https://mail.python.org/pipermail/python-ideas/2015-July/034695.html
       usage: f'{var1}' => fstr('{var1}')
              f'{var1=}' => fstr('{var1=}')
    '''
    frame = sys_getframe(level)
    formatter = evalFormatter(frame.f_globals, frame.f_locals)
    result = formatter.format(_str)
    del formatter
    return result

f = fstr

# # just for testing
# def fprint(*strs, level=1, **kwrds):
#     result = []
#     for _str in strs:
#         result.append(fstr(_str, level=level+1))
#     print(*result, **kwrds)

# ff = fprint


'''
example:
>>> f('{evalFormatter=}')
"evalFormatter=<class '__main__.evalFormatter'>"

>>> f('{debugFormatter  =}')
"debugFormatter  =<class '__main__.debugFormatter'>"

>>> f('{debugFormatter  =!r:*^48}')
"debugFormatter  =*******<class '__main__.debugFormatter'>********"

>>> f('{locals()[evalFormatter]  =!r:*>42}')
"locals()[evalFormatter]  =**********<class '__main__.evalFormatter'>"

>>> f('{input() = :*>24}')
password
'input() = ****************password'
'''


