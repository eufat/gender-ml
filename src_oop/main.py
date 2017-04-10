from libs.nltk_gender_ml import *
class Program:
    
    def main(self, *args):
        genderml = NLTKGenderML('datasets/male.csv', 'datasets/female.csv')
        genderml.show_maintenance()
        genderml.test_person_gender_by_name('Yuma Fahmi Alam')

Program().main()