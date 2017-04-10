import nltk
from read_lineByLine_toList import read_line_by_line
from find_consonants import count_consonants
from gender_last_two import *
import random

class Program:
    
    def main(self, *args):
        labeled_names = (
            [(name, 'male') for name in male_list] + 
            [(name, 'female') for name in female_list]
        )

        random.shuffle(labeled_names)

        featuresets = [(gender_features_last_two(n), gender) for (n, gender) in labeled_names]

        train_set = featuresets[500:]
        test_set = featuresets[:500]

        classifier = nltk.NaiveBayesClassifier.train(train_set)

        print ("ACCURACY IS: ")
        print (nltk.classify.accuracy(classifier, test_set))

        classifier.show_most_informative_features()

        test_name = "Aldey Wahyu Putra"
        test_name.capitalize()
        print(test_name + " is " + classifier.classify(gender_features_last_two(test_name)))




Program().main()