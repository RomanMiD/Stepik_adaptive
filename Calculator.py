#Supported operations: +, -, /, *, mod, pow, div;
from operator import truediv, mul, add, sub, mod, floordiv
def main():
    op1, op2, oper = [input() for _ in range(3)]
    op1,op2,oper = float(op1), float(op2), str(oper)
    operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv,
  'mod': mod,
  'pow': pow,
  'div': floordiv
    }


    try:
        print(operators[oper](op1, op2))
    except ZeroDivisionError:
        print("Division by 0!")
if __name__=="__main__":
    main()
