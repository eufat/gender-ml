from nltk.corpus import names
import random

# ambil kata pertama dari kalimat
def get_first_word(words):
    words_list = words.split()
    if len(words_list) > 1 :
        # kalau lebih besar dari satu kata dalam kalimat, return kata pertama
        return words_list[0]
    else:
        # kalau hanya satu kata dalam kalimat, return kata itu
        return words


def gender_features_first(word):
    word = get_first_word(word) # ambil kata pertama
    return {'first_letter': word[0]} # return huruf pertama

labeled_names = (
    [(name, 'male') for name in names.words('male.txt')] + 
    [(name, 'female') for name in names.words('female.txt')]
)

random.shuffle(labeled_names)

featuresets = [(gender_features_last(n), gender) for (n, gender) in labeled_names]

train_set = featuresets[500:]
test_set = featuresets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print ("accuracy is: ")
print (nltk.classify.accuracy(classifier, test_set))

classifier.show_most_informative_features()



