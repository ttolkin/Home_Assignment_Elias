''' 
family_tree.py  
Classes for the family tree.
Author @Elias Fauser
'''

import csv

class Person:
    def __init__(self, name, father = None, mother = None, children = [], spouse = None):
        self.name = name
        self.father = father
        self.mother = mother
        self.children = children
        self.spouse = spouse


class FamilyTree:
    def __init__(self):
        self.family = []

    def add_person(self, person):
        self.family.append(person)

    # gets the data from the .csv file. filename = the filepath (and name to)
    def load_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['Name']
                father = row['Father']
                mother = row['Mother']
                children = row['Children'].split(', ') if row['Children'] else []
                spouse = row['Spouse']

                person = Person(name, father, mother, children, spouse)
                self.add_person(person)

     # returns the parents of person_name  
    def get_parent_info(self, person_name):
        for person in self.family:
            if person.name == person_name:
                return person.mother, person.father 

    # returns the childs of person_name        
    def get_child_info(self, person_name):
        for person in self.family:
            if person.name == person_name:
                return person.children
            
    # colects the data to be printet
    def print_person_info(self, person_name):
        parents = self.get_parent_info(person_name)
        grandparents = []
        # geting the parents of the parents
        for parent in parents:
            parent_info = self.get_parent_info(parent)
            grandparents.extend(parent_info if parent_info is not None else [])
        
        childs = self.get_child_info(person_name)
        grandchilden = []
        for grandchild in childs:
            grandchilden.append(grandchild)

        # Print the family
        print(f'\nGrandparents: {", ".join(grandparents)}\n'\
              f'Parents: {", ".join(parents)}\n'\
              f'Target Name: {person_name}\n'\
              f'Childs: {", ".join(childs)}\n'\
              f'Grandshildren: {", ".join(grandchilden)}\n')
