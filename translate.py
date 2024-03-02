import re

def translate(operation):
    if "y=" in operation:
        operation_list = operation.split('=')
        operation = operation_list[1]  
    else:
        operation = operation.replace('y=', '')
    
    # operation.replace("\sin", "np.sin")

    expression = operation
    # Replace Desmos-specific functions with numpy equivalents
    # expression = re.sub(r'sin\((.*?)\)', r'np.sin(\1)', expression)
    # expression = re.sub(r'cos\((.*?)\)', r'np.cos(\1)', expression)
    # Add more replacements as needed for other functions
    
    # Replace Desmos-specific symbols with numpy equivalents
    expression = expression.replace('\\pi x', 'np.pi*x')
    expression = expression.replace('x \\pi', 'x*np.pi')
    expression = expression.replace('\\pi', 'np.pi')
    expression = expression.replace('\\cdot', '*')  # Replace \cdot with *

    expression_cpy = expression
    expression = expression.replace('\\frac{', '(')
    if expression_cpy != expression:
        expression = expression.replace('}{', ')/(')
        expression = expression.replace('}', ')')

    expression_cpy = expression
    expression = expression.replace('\\sin^{-1}', 'np.arcsin')
    expression = expression.replace('\\cos^{-1}', 'np.arccos')
    expression = expression.replace('\\tan^{-1}', 'np.arctan')
    # expression = expression.replace('\\csc^{-1}', 'np.arcsin')
    # expression = expression.replace('\\sec^{-1}', 'np.arcsin')
    # expression = expression.replace('\\cot^{-1}', 'np.arcsin')


    expression_cpy = expression
    expression = expression.replace('^{', '**(')
    if expression_cpy != expression:
        expression = expression.replace('}', ')')

    expression_cpy = expression
    expression = expression.replace('\\sqrt{', 'np.sqrt(')
    if expression_cpy != expression:
        expression = expression.replace('}', ')')

    expression = expression.replace('\\exp', 'np.e**')
    expression = expression.replace('\\ln', 'np.log')
    expression = expression.replace('\\e x', 'np.e*x')
    expression = expression.replace('x \\e', 'x*np.e')
    expression = expression.replace('\\e', 'np.e')

    #log base n

    expression = expression.replace('\\log', 'np.log10')


    


    expression = expression.replace('\\sin', 'np.sin')
    expression = expression.replace('\\cos', 'np.cos')
    expression = expression.replace('\\tan', 'np.tan')
    expression = expression.replace('\\csc', '1/np.sin')
    expression = expression.replace('\\sec', '1/np.cos')
    expression = expression.replace('\\cot', '1/np.tan')

    # expression_cpy = expression
    # expression = expression.replace('\\operatorname{lcm}\left(', 'np.lcm(np.floor(')
    # if expression_cpy != expression:
    #     expression = expression.replace(',\\', '),np.floor(')
    #     expression = expression.replace('\\right)', '))')


    expression_cpy = expression
    expression = expression.replace('\\operatorname{mod}\left(', 'np.mod(')
    if expression_cpy != expression:
        expression = expression.replace('\\right)', ')')

    expression_cpy = expression
    expression = expression.replace('\\operatorname{ceil}\left(', 'np.ceil(')
    if expression_cpy != expression:
        expression = expression.replace('\\right)', ')')
    
    expression_cpy = expression
    expression = expression.replace('\\operatorname{floor}\left(', 'np.floor(')
    if expression_cpy != expression:
        expression = expression.replace('\\right)', ')')

    expression_cpy = expression
    expression = expression.replace('\\operatorname{round}\left(', 'np.round(')
    if expression_cpy != expression:
        expression = expression.replace('\\right)', ')')
            
    expression_cpy = expression
    expression = expression.replace('\\operatorname{sign}\left(', 'np.sign(')
    if expression_cpy != expression:
        expression = expression.replace('\\right)', ')')

    #sqrt[5]{x}
    # expression_cpy = expression
    # expression = expression.replace('\\sqrt[', 'np.sign(')
    # if expression_cpy != expression:
    #     expression = expression.replace('\\right)', ')')
        

    #\operatorname{nPr}\left(x,2\right)
    # expression_cpy = expression
    # expression = expression.replace('\\operatorname{nPr}\left(', 'math.perm(np.floor(')
    # if expression_cpy != expression:
    #     expression = expression.replace(',', '), np.floor(')        
    #     expression = expression.replace('\\right)', '))')   
    expression = expression.replace('}', ')')
    expression = expression.replace('{', '(')

    expression = expression.replace('\\left', '(')
    expression = expression.replace('\\right', ')')

    for i in range(len(expression)-1):
        if (expression[i] == 'x' and (expression[i+1] == '1' or expression[i+1] == '2' or expression[i+1] == '3' or expression[i+1] == '4' or expression[i+1] == '5' or expression[i+1] == '6' or expression[i+1] == '7' or expression[i+1] == '8' or expression[i+1] == '9')) or (expression[i+1] == 'x' and (expression[i] == '1' or expression[i] == '2' or expression[i] == '3' or expression[i] == '4' or expression[i] == '5' or expression[i] == '6' or expression[i] == '7' or expression[i] == '8' or expression[i] == '9')) or (expression[i] == ')' and expression[i+1] == 'x') or (expression[i+1] == '(' and expression[i] == 'x'):
            expression = expression[:i+1]+'*'+expression[i+1:]

    
    return expression
