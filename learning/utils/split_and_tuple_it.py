import random

def split_from_listobj_and_tuple_it(listobj, attr):
    labeled_word = [(word, attr) for word in listobj]
    return labeled_word