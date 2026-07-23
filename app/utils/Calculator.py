import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}

def calculate(expression: str) -> str:
    """
    Safely evaluate a mathematical expression.
    """

    def evaluate(node):
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            return OPERATORS[type(node.op)](
                evaluate(node.left),
                evaluate(node.right)
            )

        if isinstance(node, ast.UnaryOp):
            return OPERATORS[type(node.op)](
                evaluate(node.operand)
            )

        raise ValueError("Unsupported expression")

    try:
        tree = ast.parse(expression, mode="eval")
        return str(evaluate(tree.body))

    except Exception as e:
        return str(e)