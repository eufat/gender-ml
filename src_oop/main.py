from libs.nltk_gender_ml import *
class Program:
    
    def main(self, *args):
        name = str(input("Silahkan ketikan nama:"))
        genderml = NLTKGenderML('datasets/male.csv', 'datasets/female.csv')
        genderml.show_maintenance()
        genderml.test_person_gender_by_name(name)

        x = str(input(""))

Program().main()