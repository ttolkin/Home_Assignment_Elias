''' 
main.py  
takes the input of user and prints the two generations before and after the input person
Author @Elias Fauser
'''
from family_tree import FamilyTree          

def main():
    # Create the family tree objekt
    tree = FamilyTree()

    # Load data from CSV file
    tree.load_from_csv('FamilyTree/family.csv')

    # Print information of target
    person = input('\nPlease input the name of a Person: ')
    tree.print_person_info(person)

# Runs main if the filename is main
if __name__ == '__main__':
    main()