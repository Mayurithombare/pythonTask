# math_op using function and conditions (val1,val2,op)

def math_op(val1,val2,op):
    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == '*':
        return val1 * val2
    elif op == '/':
        return val1 / val2
    else :
        return 'invalid'
 
result = math_op(10,20,'+')
print(result)

result = math_op(50,20,'-')
print(result)

result = math_op(12,4,'*')
print(result)

result = math_op(150,3,'/')
print(result)
    