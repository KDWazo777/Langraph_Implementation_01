from langchain.tools import tool

from app.utils.Calculator import calculate


@tool
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.
    
    Example:
    10+20
    5**2
    15/3
    7*8
    """

    return calculate(expression)

@tool
def no_result(expression: str) -> str:
    """
    Use this tool when the user's request is not a mathematical calculation
    or cannot be solved using the available tools.
    """

    return "No result"