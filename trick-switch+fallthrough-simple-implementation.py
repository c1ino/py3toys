def testswitch_autobreak(switch, expr):
    print('testswitch_autobreak', expr)
    '''autobreak: no fallthrough allowed'''
    for case in switch(expr):
        if case(2):
            print(f'@@case {2}: {expr}')
        elif case(1):
            print(f'@@case {1}: {expr}')
        elif case(0):
            print(f'@@case {0}: {expr}')
        else:       # default-condition
            print(f'@@case {"default"}: {expr}')
            
            
            
def testswitch_hardbreak(switch, expr):
    print('testswitch_hardbreak', expr)
    '''hardbreak: no fallthrough unless switch/case() support it'''
    for case in switch(expr):
        if case(2):
            print(f'@@case {2}: {expr}')
            break
        if case(1):
            print(f'@@case {1}: {expr}')
            break
        if case(0):
            print(f'@@case {0}: {expr}')
            break
        if 'default':       # default-condition
            print(f'@@case {"default"}: {expr}')
        # end of for-clauses
    # else:
    #     print(f'@@case {"default2"}: {expr}')
            
    
    
    
def testswitch_fallthrough(switch, expr):
    print('testswitch_hardbreak+soft-fallthrough', expr)
    '''hardbreak: fallthrough support by switch/case() '''
    for case in switch(expr, autobreak=False):
        if case(2):
            print(f'@@case {2}: {expr}')
        if case(1):
            print(f'@@case {1}: {expr}')
        if case(0):
            print(f'@@case {0}: {expr}')
        # if (hasattr(case, 'default') and case.default()) \
        # or case(case) \
        # or (hasattr(case, 'match') and not case.match) \
        # or 'default' \
        # or True \
        # or case() :
        print(f'@@case {"default"}: {expr}')
    


def testswitch_hardbreak_strict(switch, expr):
    print('testswitch_hardbreak', expr)
    '''hardbreak: no fallthrough unless switch/case() support it'''
    for case in switch(expr):
        if case(2):
            print(f'@@case {2}: {expr}')
            break
        if case(1):
            print(f'@@case {1}: {expr}')
            break
        if case(0):
            print(f'@@case {0}: {expr}')
            break
        # end of for-clauses
    else:
        print(f'@@case {"default"}: {expr}')



def print_title(*args, **kwrds):
    print('='*48)
    print(*args, **kwrds)



expr = 1
    

# ============================================================
print_title('#ver1, without any function/lambda/class/instance')
'''compatible with both autobreak and hardbreak style'''
for case in [expr]:
    if case == 1:
        print(f'@@case {1}: {expr}')
        break
    if case == 2:
        print(f'@@case {2}: {expr}')
        break

         
         
# ============================================================
print_title('#ver2-light, with lambda')
def switch(expr):
    return (lambda case: case==expr, )
# switch = lambda _expr: (lambda case: case==_expr, ) 

sw_lambda = switch
    
    
testswitch_autobreak(sw_lambda, 2)
testswitch_hardbreak(sw_lambda, 2)
# testswitch_fallthrough(sw_lambda, 2)
testswitch_autobreak(sw_lambda, 9)
testswitch_hardbreak(sw_lambda, 9)
# testswitch_fallthrough(sw_lambda)




# ============================================================
print_title('#ver3, with function')
    
def switchor(expr, autobreak=True):
    '''see also: https://code.activestate.com/recipes/410692/
       (support multi-expressions in single case, e.g. case(1, 'a', 2, 'b'))
    '''
    match = False
    def self(*cases):
        nonlocal match, autobreak, expr, self
        if match and autobreak:
            return False
        # elif not cases:       # optional: explicit-default-condition; usage: case()
            # return True
        match = True if match else expr in cases
        return match
    return (self, )

sw_func = switchor

      
testswitch_autobreak(sw_func, 2)
testswitch_hardbreak(sw_func, 2)
testswitch_fallthrough(sw_func, 2)
testswitch_autobreak(sw_func, 9)
testswitch_hardbreak(sw_func, 9)
testswitch_fallthrough(sw_func, 9)

    
    
    

# ============================================================
print_title('#ver4, with class')

class switcher():
    def __init__(self, expr, autobreak=True):
        self.value = expr
        self.match = False
        self.autobreak = autobreak          # optional: autobreak-support
    def __iter__(self):
        yield self
    def __call__(self, case):
        if self.match and self.autobreak :  # optional: autobreak-support
            return False
        self.match = True if self.match else case == self.value
        # if case == self:            # optional: explicit-default-condition; usage: case(case)
            # return True if not self.autobreak else not self.match
        return self.match
    # def default(self):              # optional: explicit-default-condition; usage: case.default()
        # return True if not self.autobreak else not self.match
    pass    
    
    
sw_class = switcher

    
testswitch_autobreak(sw_class, 2)
testswitch_hardbreak(sw_class, 2)
testswitch_fallthrough(sw_class, 2)

testswitch_autobreak(sw_class, 9)
testswitch_hardbreak(sw_class, 9)
testswitch_fallthrough(sw_class, 9)


    
   