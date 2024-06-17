import numpy as np

class EquationBot:
    def __init__(self, equations, constants):
        self.equations = np.array(equations)
        self.constants = np.array(constants)
        
    def solve(self):
        try:
            solution = np.linalg.solve(self.equations, self.constants)
            return solution
        except np.linalg.LinAlgError as e:
            return str(e)
          # Example Equations: 
# 2w + x - y + 3z 

equations = [
    [2, 1, -1, 3],
    [4, -2, 2, 1],
    [3, -3, 1, 2],
    [1, 1, 1, 1]
]

constants = [8, 2, 4, 5]

solver = EquationSolver(equations, constants)
solution = solver.solve()
print("Solution:", solution)
