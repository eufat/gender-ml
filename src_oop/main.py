from libs.nltk_gender_ml import *
class Program:
    
    def main(self, *args):
        repeat = True
        while repeat == True:
        
            genderml = NLTKGenderML('datasets/male.csv', 'datasets/female.csv')
            genderml.show_maintenance()
            name = str(input("Silahkan ketikan nama:"))
            genderml.test_person_gender_by_name(name)

            prompt = str(input("Ingin mencoba kembali?"))
            print("\n")
            if prompt not in ("Yes", "True", "Okay", "yes", "true", "okay", "Ok", "ok"): repeat = False

Program().main()