import streamlit as st

# Operator precedence and associativity
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
right_associative = {'^'}

def is_operator(c):
    return c in precedence

def higher_precedence(op1, op2):
    if op1 not in precedence or op2 not in precedence:
        return False
    return precedence[op1] > precedence[op2] or (precedence[op1] == precedence[op2] and op1 not in right_associative)


# Infix to Postfix Conversion
def infix_to_postfix(expression):
    stack = []
    output = []
    for char in expression:
        if char == ' ':  # Ignore spaces
            continue
        elif char.isalnum():  # If operand, append to output
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '(' off the stack
        else:  # If operator, process according to precedence
            while (stack and stack[-1] != '(' and higher_precedence(stack[-1], char)):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)


# Infix to Prefix Conversion
def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = ['(' if char == ')' else ')' if char == '(' else char for char in expression]
    postfix = infix_to_postfix(expression)
    return postfix[::-1]

# Evaluate Postfix Expression
def evaluate_expression(expression, notation_type):
    stack = []
    if notation_type == 'postfix':
        tokens = expression.split()  # Split the expression into tokens
        iterate_over = tokens  # In postfix, iterate over the tokens from left to right
    else:
        tokens = expression.split()  # Split the expression into tokens
        tokens.reverse()  # Reverse the tokens for prefix evaluation
        iterate_over = tokens  # In prefix, iterate over the reversed tokens

    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",  # Use floating-point division
        '^': lambda x, y: x ** y
    }

    for token in iterate_over:
        if token.isdigit():  # If the token is an operand
            stack.append(float(token))  # Store numbers as floats to handle decimal operations
        elif token in operators:  # If the token is an operator
            if len(stack) < 2:
                return "Error: Malformed expression"
            if notation_type == 'postfix':
                b = stack.pop()
                a = stack.pop()
            else:  # For prefix, reverse the order of operands
                a = stack.pop()
                b = stack.pop()
            if token in operators:
                result = operators[token](a, b)
                if isinstance(result, str):
                    return result  # Return error message if any
                stack.append(result)
            else:
                return "Error: Unsupported operator"
        else:
            return "Error: Unsupported operator or non-digit character"

    if len(stack) != 1:
        return "Error: Malformed expression"
    return stack.pop()



# Streamlit interface
st.title("Expression Converter and Evaluator")

# Conversion interface
with st.expander("Infix to Postfix/Prefix Conversion"):
    expression = st.text_input("Enter your infix expression", "A*B+C/D")
    if st.button('Convert to Postfix'):
        result = infix_to_postfix(expression)
        st.write("Postfix Expression: ", result)
    if st.button('Convert to Prefix'):
        result = infix_to_prefix(expression)
        st.write("Prefix Expression: ", result)

# Evaluation interface
with st.expander("Evaluate Postfix or Prefix Expression"):
    expr_eval = st.text_input("Enter expression to evaluate (ensure to separate all items with spaces)", "+ - 2 7 * 8 / 4 12")
    notation = st.selectbox("Select notation type", ('postfix', 'prefix'))
    if st.button('Evaluate Expression'):
        result = evaluate_expression(expr_eval, notation)
        st.write("Evaluated Result: ", result)


# Run this script using: streamlit run script_name.py
