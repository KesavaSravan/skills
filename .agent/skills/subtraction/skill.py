def execute(a: float, b: float) -> float:
    """
    Subtracts the second number from the first number and returns the difference.
    
    Args:
        a (float): The first number (minuend).
        b (float): The second number to subtract (subtrahend).
        
    Returns:
        float: The difference between a and b.
    """
    return float(a - b)

class SubtractionSkill:
    """
    A class wrapper for the subtraction skill to support frameworks that require
    instantiable skill classes (such as OpenClaw or BaseSkill patterns).
    """
    def __init__(self):
        self.name = "subtraction"
        self.description = "Calculates the difference between two numeric inputs."

    def run(self, a: float, b: float) -> float:
        return execute(a, b)

    async def execute(self, a: float, b: float) -> float:
        return execute(a, b)
