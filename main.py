import sys
from gauss_solver import input_matrix, normalize, eliminate, back_substitution, analyze_result, save_to_file

class App:
    def __init__(self):
        self.solver = GaussSolver()

    def run(self):
        self.menu()