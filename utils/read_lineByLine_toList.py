from pathlib import Path
# v0.0.1
# using Python 3.5

__name__ = '__read_lineByLine__'
__version__ = '0.1'

def readLineByLine(filepath):
    '''
    [Function]
    Desc: Read Line by line to array from file
    Version = 0.1
    (c) Aldey W Putra
    '''
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