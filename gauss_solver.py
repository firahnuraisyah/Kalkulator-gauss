import numpy


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
        pass

    def save_to_file(self):
        pass