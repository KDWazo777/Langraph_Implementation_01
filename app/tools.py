from langchain.tools import tool

from app.utils import calculate


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