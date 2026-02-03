'''3. Variable Scope Problem
      Input: None
      Output: UnboundLocalError: local variable 'x' referenced before assignment'''

def print_number():
    print(x)
    x = 10
print_number()