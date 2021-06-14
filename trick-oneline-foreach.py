# @echo off
# rem='''
# set pythonioencoding=utf8
# python -i -x "%~f0" %*
# exit /b 
# '''

from pprint import pprint as pp



'iter all items and multi exprs in one line lambda'
ls = dir()
# ls = globals().items()

'None exprs chain'
any(pp(x) or input('press to continue') or print() for x in ls)
any(pp(x) or input('press to continue') or print() and 0 for x in ls)
all(pp(x) or input('press to continue') or print() or 1 for x in ls)
# t = lambda:all(pp(x) or input('press to continue') or 1 for x in ls)
# t = lambda:all(pp(x) or input('press to continue') or print() or 1 for x in ls)

'Whatever exprs chain'
all((pp(x), input('press to continue'), print()) for x in ls)
# t = lambda:all((pp(x), input('press to continue')) for x in ls)
# t = lambda:all((pp(x), input('press to continue'), print()) for x in ls)

'OR human readable'
all(1 for x in ls if (pp(x), input('press_to_continue'), print()))
'AND combine condition'
all(1 for x in ls if x!=None and (pp(x), input('press_to_continue'), print()))


'abstract'
all(FLAG1 for x in ls if COND and (EXPRS,))
all(FLAG1 for x in ls if (EXPRS,))
all((EXPRS,) for x in ls)
all(NEXPRS or FLAG1 for x in ls)
any(NEXPRS and FLAG0 for x in ls)
any(NEXPRS for x in ls)
    all(NEXPR1 or NEXPRN or FLAG1 for x in ls)
    any(NEXPR1 or NEXPRN and FLAG0 for x in ls)
    any(NEXPR1 or NEXPRN for x in ls)


'nested'
all((EXPRS2,) for x in ls for y in (EXPRS1,))
all((EXPRS3,) for x in ls for y in (EXPRS1,) for z in (EXPRS2,))
    all((input(z),) for x in ls for y in (str(x),) for z in (y.replace("'", ''),))
    all((print(z),) for x in ls for y in (input('y='),) for z in (id(y),))

'nested-abstract'
all((EXPRS3,) for x in ls for y in (ASSIGNS1,) for z in (ASSIGNS2,))
all((EXPRS3,) for x in ls for y1,y2 in (ASSIGN1A,ASSIGN1B) for z1,z2 in (ASSIGN2A,ASSIGN2B))
    all((y[0],z[1]) for x in ls for y in ((A1A,A1B),) for z in ((A2A,A2B),))

for x in ls:
    Y1 = ASSIGN1A
    Y2 = ASSIGN1B
    for y in ((Y1,Y2),):
        Z1 = ASSIGN2A
        Z2 = ASSIGN2B
        for z in ((Z1,Z2),):
            EXPR3A
            EXPR3N

for x in ls:
    for y in ((ASSIGN1A,ASSIGN1B),):
        for z in ((ASSIGN2A,ASSIGN2B),):
            # EXPR3A = y[0]
            # EXPR3N = z[1]
            yield y[0], z[1]

for x in ls:
    y = (ASSIGN1A,ASSIGN1B)
    z = (ASSIGN2A,ASSIGN2B)
    yield y[0], z[1]
    # y1,y2 = (ASSIGN1A,ASSIGN1B)
    # z1,z2 = (ASSIGN2A,ASSIGN2B)
    # yield y1, z2


# (lambda:all((print(i,x),input()) for i,x in enumerate(d)))()
ppe = lambda y:all((print(i,x),input()) for i,x in enumerate(y))
# ppf = lambda y:all(ppe(filter(lambda x:x.endswith(k), paths)) or 1 for k in y)
ppf = lambda y:all(print(k) or ppe(filter(lambda x:x.endswith(k), paths)) or 1 for k in y)

# find = lambda k,y:filter(lambda x:x.endswith(k),y)
find = lambda k,y:((i,x) for i,x in enumerate(y) if x.endswith(k))
# find = lambda y:(i,x for i,x in enumerate(y) if expr(x))
# find = lambda y,expr,k:(i,x for i,x in enumerate(y) if expr(x, k))

ppc = lambda i,y,n=2:pp(y[i-n:i+n+1])

# ppf = lambda y:all((,input()) for x in y)
# ppf = lambda y:all((ppc(z[0], paths),input()) for x in y for z in find(x, paths))
# ppf = lambda y,t,n=2:all((print(x),ppc(z[0], t, n=n),input()) for x in y for z in find(x, t))
# ppf = lambda y,t,n=2:all((ppc(z[0], t, n=n),input()) for x in y if (print(x),) for z in find(x, t))
ppf = lambda a,b,n=2:all((ppc(z[0], b, n=n),input(z[0])) for x in a if (print(x),) for z in find(x, b))





'''
'''
all((EXPRS,) for x in ls)
all((EXPRS,) for x in ls if CONTINUE)
all((EXPRS,) for x in ls for y in (ASSIGN_Y,))
all((EXPRS,) for x in ls for y in ((ASSIGN_Y0,Y1),))
all((EXPRS,) for x in ls for y in (ASSIGN_Y,) if CONTINUE_Y)
all((EXPRS,) for x in ls if CONTINUE_X for y in (ASSIGN_Y,) if CONTINUE_Y)
    all((print(x,y),) for x in ls for y in (input('y='),) if y!='skip')

all((
    EXPR1,
    EXPRN,
    ) for x in ls 
    if NOT_CONTINUE_X 
        for y in ((
            ASSIGN_Y1,
            ASSIGN_Y2,
            ),)
        if NOT_CONTINUE_Y
)