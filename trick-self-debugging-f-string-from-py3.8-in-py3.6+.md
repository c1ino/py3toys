# Roughly implement pseudo-f-string that support Python 3.8 feature f-strings=debugging-specifier for Python 3.6+


## Advantages
- "printf-style" debugging convenience

## Disadvantages
- untested, unreliable
- no linting
- performance cost of `sys._getframe`
- `sys._getframe` is not guaranteed to exist in all implementations of Python.
- etc.

## Reference
- https://mail.python.org/pipermail/python-ideas/2015-July/034695.html
- https://bugs.python.org/issue36817
- https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging