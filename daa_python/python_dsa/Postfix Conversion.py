from Stack import Stack

def postfix_conversion(expr):
    stk = Stack()
    operators = ['*', '.', '%', '^', '+', '-', '/']
    brackets = ['(', ')', '{', '}', '[', ']']
    for i in expr:
        if i in brackets:
            continue
        if i in operators:
            sec = stk.pop()
            fst = stk.pop()
            val = eval(f'{fst}{i}{sec}')
            stk.push(val)
        else:
            conv = int(i)
            if conv in range(0, 10):
                stk.push(i)
    return stk.pop()

expr = '72-4*28-*6/'
print(postfix_conversion(expr))
