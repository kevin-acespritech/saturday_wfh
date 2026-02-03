'''3. Variable Scope Problem
Input: None
Output: UnboundLocalError: local variable 'x' referenced before assignment'''

def variable_function():
    print(x)
    x = 565
variable_function()
