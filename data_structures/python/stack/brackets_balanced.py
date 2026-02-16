from Stack import Stack


def brackets_balanced(brackets_string: str) -> bool:
    stack = Stack()
    for bracket in brackets_string:
        if bracket == ')' and stack.peek() is None:
            return False
        if bracket == ')' and stack.peek() == '(':
            stack.pop()
        else:
            stack.push(bracket)

    if stack.size() == 0:
        return True
    else:
        return False
