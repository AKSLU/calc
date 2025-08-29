def calc(expr):
    try:
        a, op, b = expr.split()
        a, b = float(a), float(b)
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b if b != 0 else 'на 0 нельзя'
        return 'ошибка'
    except: return 'ошибка'


        

