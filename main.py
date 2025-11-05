import sys
from gauss_solver import input_matrix, normalize, eliminate, back_substitution, analyze_result, save_to_file

class App:
    def __init__(self):
        self.solver = GaussSolver()
        self.user = UserLogin()

    def run(self):
        if self.user.login():
            self.menu()
