def read_line_by_line(filepath):
    koleksi_nama = list()
    with open(filepath) as f:
        for line in f:
            koleksi_nama.append(line)
            koleksi_nama = [x.strip() for x in koleksi_nama]
        if type(koleksi_nama) is list:
            return koleksi_nama
        else:
            print("Data type is not list")
            return "ERR_01"
