from pathlib import Path
# v0.0.1

__name__ = "Read line by line and store it to List"
__version__ = '0.1'

def readLineByLine(filepath):
    koleksi_nama = list()

    path = Path(filepath)
    if path.is_file():
        print("File {0} ditemukan!".format(filepath))
        with open(filepath) as f:
            for line in f:
                koleksi_nama.append(line)
                koleksi_nama = [x.strip() for x in koleksi_nama]
        if type(koleksi_nama) is list:
            print("Selamat! Tipe objek ini ialah List!")
            return koleksi_nama
            '''for test in koleksi_nama:
                print(test)'''
                
        else:
            return "ERR_01"
    else:
        print("Maaf, file tersebut tidak ditemukan!")