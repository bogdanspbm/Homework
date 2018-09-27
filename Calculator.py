def Calc(action,a,b):
    try:
       calculator_actions = {
          '*': a * b,
          '/': a / b,
          '+': a + b,
          '-': a - b,
          '**': a ** b,
       }
       return calculator_actions[action]
    except:
       if b == 0 and (action == '*' or action == '/' or action == '-' or action == '+' or action == '**'):
          return 'Infinity'
       else:
          return 'Unknown operation'


#print(Calc('!',2,0))