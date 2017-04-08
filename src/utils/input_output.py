from os.path import dirname, split, isdir
from os import path

def get_src_path():
    global parent_dir
    src = path.abspath(__file__)
    parent_dir = lambda x: split(x)[0] if isdir(x) else split(dirname(x))[0]
    return parent_dir(src)

print(get_src_path())