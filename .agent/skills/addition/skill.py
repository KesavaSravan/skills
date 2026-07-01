def execute(a: float, b: float) -> float:
    """
    Adds two numbers together and returns the sum.
    
    Args:
        a (float): The first number.
        b (float): The second number.
        
    Returns:
        float: The sum of a and b.
    """
    return float(a + b)

class AdditionSkill:
    """
    A class wrapper for the addition skill to support frameworks that require
    instantiable skill classes (such as OpenClaw or BaseSkill patterns).
    """
    def __init__(self):
        self.name = "addition"
        self.description = "Calculates the sum of two numeric inputs."

    def run(self, a: float, b: float) -> float:
        return execute(a, b)

    async def execute(self, a: float, b: float) -> float:
        return execute(a, b)
