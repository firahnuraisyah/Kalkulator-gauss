from gauss_solver import GaussSolver
print("="*70 + "\n" + "WELCOME TO KALKULATOR GAUSS" + "\n" + "MATH IS EASIER" + "\n" + "="*70)
if __name__ == "__main__":
    solver = GaussSolver()
    solver.input_ordo_matrix()
    solver.normalize()
    solver.eliminate()
    solver.back_substitution()
    solver.show_process()
    solver.analyze_result()
    solver.save_to_file()   
print("="*70 + "\n" + "THANK YOU FOR TRUSTING CALCULATOR GAUSS" + "\n" + "AP-4" + "\n" + "="*70)