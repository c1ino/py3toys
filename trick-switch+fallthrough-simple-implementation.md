
# Simple switch construction with lambda+for+break+if instead of dictionary/attribute-based dispatch in Python3

## About `switch(){…}`
| `switch(){…}` | equivalence |
| ------------- | ----------- |
| `case:`       | match       |
| `default:`    | not match   |
| fallthrough   | not `break` |


## About "`break`-style"
| `break`-style: | `if-elif-else` | `case-break`  | (IDK)                                            |
| -------------- | -------------- | ------------- | ------------------------------------------------ |
| equivalence    | autobreak      | hardbreak     | softbreak                                        |
| description    | implicit-break | explict-break | skip-`if case(v1):`-by-`case(v1)`-return-`False` |
| `case:`        | yes            | yes           | yes                                              |
| `default:`     | yes            | yes           | yes                                              |
| fallthrough    | no             | prerequisite  | could                                            |


## Basic framework
```python
# autobreak
for case in switch(expr):
    if case('c1'):
        print('case 1!')
    elif case('c2'):
        print('case 2!')
    else:
        print('case default!')

# hardbreak
for case in switch(expr):
    if case('c1'):
        print('case 1!')
        break
    if case('c2'):
        print('case 2!')
        break
    # if 'default':
    print('case default!')

# softbreak with fallthrough
for case in switch(expr, fallthrough=True):
    if case('c1'):
        print('case 1 and fallthrough!')
        # break
    if case('c2'):
        print('case 2 and fallthrough!')
        # break
    if case() or case.default() or 'default':    # depends on switch()-implementation
        print('case default!')
# else:     # 
#     print('case default!')
```


## About `switch()` implementation
| by:                             | `lambda` | `class` | nested-`function` | (remark)                                                       |
| ------------------------------- | -------- | ------- | ----------------- | -------------------------------------------------------------- |
| `case:`                         | yes      | yes     | yes               |                                                                |
| fallthrough                     | no       | could   | could             | by `if matched: return True;`                                  |
| soft-`default:`                 | no       | could   | could             | by `if arg == 'specific_value_or_empty': return True;`         |
| multi-values-in-single-`case:`  | could    | could   | could             | by `case(*args): if val in args;`                              |
| flexible-compare                | no       | could   | could             | by `case('c1', cmp=func_cmp): if cmp(val, 'c1'): return True;` |
| strict-mode-only-one-`default:` | no       | could   | could             |                                                                |


## Advantages and disadvantages
Advantages:
- trick
- lambda in one-line
- a bit readability 
- without define case-branch functions in advance
- fallthrough

Disadvantages:
- no guarantee
- no linting
- performance worse than dispath dictionaries
- confusing
- etc.


## Usage
> (IDK)


## See also & reference
- https://code.activestate.com/recipes/410692/
- PyPI packages that support switch-case
- switch by dictionary/attribute-based dispatch
- https://www.python.org/dev/peps/pep-3103/
- https://docs.python.org/2/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python
- https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
- https://www.python.org/dev/peps/pep-0634/
- https://en.wikipedia.org/wiki/Switch_statement
- https://github.com/chinesehuazhou/python-whydo/blob/master/zh_CN/17%E3%80%81Python%20%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E6%94%AF%E6%8C%81%20switch%20%E8%AF%AD%E5%8F%A5%EF%BC%9F.md
