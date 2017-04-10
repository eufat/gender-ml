import nltk
from lib.iosystem import IOSystem
from lib.sentence_system import SentenceSystem
from lib.nltk_gender_ml import NLTKGenderML
import random

class Program:
    
    def main(self, *args):
        genderml = NLTKGenderML()
        genderml.show_maintenance()
        genderml.test_person_gender_by_name('Femilia')

Program().main()