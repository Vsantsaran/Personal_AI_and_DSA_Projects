from Stack import Stack

def match(expr, s_dict):
    stk = Stack()
    for i in expr:
        if i in s_dict.values():
            stk.push(i)
        elif i in s_dict.keys():
            if not stk.is_empty():
                if stk.pop() != s_dict[i]:
                    return False
            else:
                return False
    return stk.is_empty()

expr = input('Enter an expression: ')
symbol_dict = {')': '(', '}': '{', ']': '['}
if match(expr, symbol_dict):
    print('Expression correct.')
else:
    print('Expression incorrect.')