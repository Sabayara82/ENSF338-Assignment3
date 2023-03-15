import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data


def is_atom(expr):
    return not isinstance(expr, list)


def parse_expression(expr):
    result = None  # Initialize result to None
    if is_atom(expr):
        result = int(expr)
    else:
        op = expr[0]
        if op == "+":
            left_operand = parse_expression(expr[1])
            right_operand = parse_expression(expr[2])
            result = left_operand + right_operand
        elif op == "-":
            left_operand = parse_expression(expr[1])
            right_operand = parse_expression(expr[2])
            result = left_operand - right_operand
        elif op == "*":
            left_operand = parse_expression(expr[1])
            right_operand = parse_expression(expr[2])
            result = left_operand * right_operand
        elif op == "/":
            left_operand = parse_expression(expr[1])
            right_operand = parse_expression(expr[2])
            result = left_operand / right_operand
        else:
            print("Invalid operator:", op)
    return result


def tokenize(expr):
    tokens = []
    current_token = ''
    for c in expr:
        if c == ' ':
            if current_token:
                tokens.append(current_token)
                current_token = ''
        elif c == '(' or c == ')':
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(c)
        else:
            current_token += c
    if current_token:
        tokens.append(current_token)
    return tokens


def parse_tokens(tokens):
    stack = Stack()
    for token in tokens:
        if token == '(':
            stack.push(token)
        elif token == ')':
            sub_expr = []
            while stack.peek() != '(':
                sub_expr.insert(0, stack.pop())
            stack.pop()  # Remove the '(' from the stack
            stack.push(parse_expression(sub_expr))
        else:
            stack.push(token)
    return stack.pop()


if __name__ == '__main__':
    expr = sys.argv[1]
    tokens = tokenize(expr)
    result = parse_tokens(tokens)
    print(result)
