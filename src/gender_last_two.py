import nltk
from read_lineByLine_toList import read_line_by_line
from find_consonants import count_consonants
import random

male_list = read_line_by_line('datasets/male.csv')
female_list = read_line_by_line('datasets/female.csv')

# ambil kata pertama dari kalimat
def get_first_word(words):
    words_list = words.split()
    if len(words_list) > 1 :
        # kalau lebih besar dari satu kata dalam kalimat, return kata pertama
        return words_list[0]
    else:
        # kalau hanya satu kata dalam kalimat, return kata itu
        return words

def gender_features_last_two(word):
    word = get_first_word(word) # ambil kata pertama
    return {'last_two':  word[-2:]} # return huruf 2 kata terakhir

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

test_name = "aldey Wahyu Putra"
test_name.capitalize()
print(test_name + " is " + classifier.classify(gender_features_last_two(test_name)))


