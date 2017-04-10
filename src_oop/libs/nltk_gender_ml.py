import nltk
from .io_system import *
from .sentence_system import *
import random

class NLTKGenderML:
    __instance__ = 0

    def __init__(self, dataset_male, dataset_female):
        NLTKGenderML.__instance__ += 1
        iosys = IOSystem()
        self.male_list = iosys.read_line_to_list(dataset_male)
        self.female_list = iosys.read_line_to_list(dataset_female)
        
        self.labeled_names = (
            [(name, 'male') for name in self.male_list] + 
            [(name, 'female') for name in self.female_list]
        )
        random.shuffle(self.labeled_names)

        self.featuresets = [(self.gender_features_last_two(n), gender) for (n, gender) in self.labeled_names]
        
        self.train_set = self.featuresets[500:]
        self.test_set = self.featuresets[:500]

        self.classifier = nltk.NaiveBayesClassifier.train(self.train_set)


    # ambil kata pertama dari kalimat
    def get_first_word(self, words):
        words_list = words.split()
        if len(words_list) > 1 :
            # kalau lebih besar dari satu kata dalam kalimat, return kata pertama
            return words_list[0]
        else:
            # kalau hanya satu kata dalam kalimat, return kata itu
            return words

    def gender_features_last_two(self, word):
        word = self.get_first_word(word) # ambil kata pertama
        return {'last_two':  word[-2:]} # return huruf 2 kata terakhir

    def show_maintenance(self):
        print ("ACCURACY IS: ")
        print (nltk.classify.accuracy(self.classifier, self.test_set))
        self.classifier.show_most_informative_features()

    def test_person_gender_by_name(self, name):
        test_name = name
        test_name.capitalize()
        print(test_name + " is " + self.classifier.classify(self.gender_features_last_two(test_name)))
