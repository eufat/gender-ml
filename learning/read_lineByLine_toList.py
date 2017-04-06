from pathlib import Path
# v0.0.1

__name__ = "Read line by line and store it to List"
__version__ = '0.1'

def readLineByLine(filepath):
    koleksi_nama = []

    path = Path(filepath)
    if path.is_file():
        print("File {0} ditemukan!".format(filepath))
        with open(filepath) as f:
            for line in f:
                koleksi_nama = list.append(line)

        if type(koleksi_nama) is list:
            print("Type is a list")
            return koleksi_nama
        else:
            return "ERR_01"
    else:
        print("Maaf, file tersebut tidak ditemukan!")
