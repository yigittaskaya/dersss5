"""
import os
print(os.getcwd())
os.chdir("C:/Users/egitim.sinif2")
print(os.listdir())
os.mkdir("deneme1")
"""
import os
def klasor_olustur(x):
    for i in range(x):
        os.mkdir("virüs"+str(i+1))
sayi=int(input("kaç tane klasör oluşturulsun"))
klasor_olustur(sayi)
