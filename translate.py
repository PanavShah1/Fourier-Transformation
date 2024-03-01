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
    expression = expression.replace('π', 'np.pi')
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
    if expression_cpy != expression:
        expression = expression.replace('}', ')')

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
    expression = expression.replace('\\e', 'np.e')

    


    expression = expression.replace('\\sin', 'np.sin')
    expression = expression.replace('\\cos', 'np.cos')
    expression = expression.replace('\\tan', 'np.tan')
    expression = expression.replace('\\csc', '1/np.sin')
    expression = expression.replace('\\sec', '1/np.cos')
    expression = expression.replace('\\cot', '1/np.tan')

    expression = expression.replace('\\left', '(')
    expression = expression.replace('\\right', ')')
    # Add more replacements as needed for other symbols
    
    return expression
