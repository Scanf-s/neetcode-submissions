class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        buffer: list[int] = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:

                if len(buffer) < 2:
                    return 0

                num1: int = buffer.pop()
                num2: int = buffer.pop()

                if token == '+':
                    buffer.append(num1 + num2)
                elif token == '-':
                    buffer.append(num2 - num1)
                elif token == '*':
                    buffer.append(num1 * num2)
                else:
                    if num1 == 0:
                        buffer.append(0)
                    else:
                        buffer.append(int(num2 / num1))
            else:
                buffer.append(int(token))
                
        return buffer[-1] if buffer else 0
