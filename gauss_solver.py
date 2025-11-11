import numpy as np
import datetime

class GaussSolver:
    def __init__(self):
        self.matrix = []
        self.K = 0          
        self.B = 0           
        self.is_numpy = False
        self.history = []   

    def input_ordo_matrix(self):
        while True:
            while True :
                try :
                    self.K = int(input("Masukkan Jumlah Variabel : "))
                    if self.K <= 0 :
                        print("Jumlah Harus Positif.")
                        continue
                    break
                except ValueError :
                    print("TETOT! Harap masukkan bilangan bulat.")
                    
            while True :
                try :
                    self.B = int(input("Masukkan Jumlah Baris : "))
                    if self.B <= 0 :
                        print("Jumlah Harus Positif.")
                        continue
                    break
                except ValueError :
                    print("TETOT! Harap masukkan bilangan bulat.")
                    
            if self.K != self.B :
                print("\nMaaf saat ini kami hanya menyediakan program untuk matriks persegi.")
                print("\nAdapun penyebab yang membatasi program ini hanya untuk matriks persegi adalah inkonsistensi result : ")
                print("1. Saat jumlah baris lebih besar dari jumlah variabel (kolom)")
                print("2. Saat jumlah variabel (kolom) lebih besar dari jumlah baris\n")   
                self.K = 0
                self.B = 0
                while True:
                    ulang = input("\nApakah Anda ingin mencoba lagi? (y/n): ").strip().lower()
                    if ulang == "y":
                        print("\nSilakan masukkan kembali ordo matriks yang persegi.\n")
                        break  
                    elif ulang == "n":
                        print("\nProgram dihentikan.")
                        exit()  
                    else:
                        print("Masukkan hanya 'y' atau 'n' saja.")
                        continue
                continue
            break       

    def normalize(self):
        pass

    def eliminate(self):
        pass

    def back_substitution(self):
        pass

    def show_process(self):
        pass

    def analyze_result(self):
        if not isinstance(self.matrix, np.ndarray):
            print("Matriks belum siap untuk analisis.")
            return
        A = self.matrix[:, :-1]
        rank_A = np.linalg.matrix_rank(A)
        rank_Ab = np.linalg.matrix_rank(self.matrix)
        n = A.shape[1]

        print("\n===== ANALISIS HASIL =====")
        if rank_A < rank_Ab:
            print("➡ Sistem tidak memiliki solusi (inkonsisten).")
            hasil = "Tidak ada solusi (inkonsisten)."
        elif rank_A == rank_Ab == n:
            print("➡ Sistem memiliki solusi tunggal.")
            hasil = "Sistem memiliki solusi tunggal."
        self.history.append("\nAnalisis Hasil:\n" + hasil)

    def save_to_file(self):
        pass