# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i+1))

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) > 0 and opening_brackets_stack[-1].Match(next):
                d = opening_brackets_stack.pop()
            else:
                opening_brackets_stack.append(Bracket(next, i+1))
                break

    if len(opening_brackets_stack) == 0: print("Success")
    else: print(opening_brackets_stack[-1].position)
