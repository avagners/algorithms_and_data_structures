from Stack import Stack

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def calc_postfix_expression(input_stack: Stack, operators=OPERATORS):
    result = Stack()
    while input_stack.size() > 0:
        item_input_stack = input_stack.pop()
        if item_input_stack == '=':
            return result.peek()
        if item_input_stack in operators:
            num1 = result.pop()
            num2 = result.pop()
            result.push(operators[item_input_stack](num2, num1))
        else:
            result.push(int(item_input_stack))
    return result.peek()
