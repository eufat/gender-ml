import libs.nltk_gender_ml
class Program:
    
    def main(self, *args):
        genderml = libs.nltk_gender_ml.NLTKGenderML('datasets/male.csv', 'datasets/female.csv')
        genderml.show_maintenance()
        genderml.test_person_gender_by_name('Yuma Fahmi Alama')

Program().main()