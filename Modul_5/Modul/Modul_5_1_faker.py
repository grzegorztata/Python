from faker import Faker

class Person:
    def __init__(self, first_name, last_name, company, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.occupation = occupation
        self.email = email

fake = Faker()

# Create a list of five people with randomly generated attributes
people = []
for i in range(5):
    person = Person(
        fake.first_name(),
        fake.last_name(),
        fake.company(),
        fake.job(),
        fake.email()
    )
    people.append(person)

for person in people:
    print("First Name:", person.first_name)
    print("Last Name:", person.last_name)
    print("Company:", person.company)
    print("Occupation:", person.occupation)
    print("Email:", person.email)
    print("--------------------")